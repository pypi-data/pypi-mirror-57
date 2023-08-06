'''
Created on 2016/3/8

:author: hubo
'''
from vlcp.config import defaultconfig
from vlcp.service.connection.tcpserver import TcpServerBase
from vlcp.protocol.redis import Redis
from vlcp.server.module import api
from vlcp.utils.redisclient import RedisClient, RedisConnectionDown
from vlcp.event.runnable import RoutineContainer
from vlcp.event.lock import Lock
from zlib import compress, decompress, error as zlib_error
import pickle
from contextlib import closing
from vlcp.utils.kvcache import KVCache
try:
    import cPickle
except ImportError:
    pass
import json
from vlcp.utils.jsonencoder import encode_default, decode_object
import itertools
try:
    from itertools import izip
except ImportError:
    def izip(*args, **kwargs):
        return iter(zip(*args, **kwargs))

import random
from time import time

class RedisWriteConflictException(Exception):
    pass

@defaultconfig
class RedisDB(TcpServerBase):
    '''
    Create redis clients to connect to redis server
    '''
    # Default Redis connection URL
    _default_url = 'tcp://localhost/'
    # Default database selected
    _default_db = None
    # Default serialization protocol: should be "json" or "pickle"
    _default_serialize = 'json'
    # Use deflate to compress the serialized data
    _default_deflate = True
    # Pickling version: should be a number or "default"/"highest"
    _default_pickleversion = 'default'
    # Allow using cPickle
    _default_cpickle = True
    # Serialize requests on the same key in this process if a transact rolls back too many times
    _default_enterseq = 20
    # Try to use locks on the same key for all VLCP processes if a transact rolls back too many times
    _default_enterlock = 50
    # Maximum retry times for a transact
    _default_maxretry = 160
    client = True
    def __init__(self, server):
        self._redis_clients = {}
        TcpServerBase.__init__(self, server, Redis)
        self._sequencial = False
        self._sequencialsince = time()
        self._enterlock = False
        self._enterlocksince = time()
        if self.serialize == 'pickle' or self.serialize == 'cpickle' or self.serialize == 'cPickle':
            if self.serialize == 'pickle':
                if not self.cpickle:
                    p = pickle
                else:
                    p = cPickle
            else:
                p = cPickle
            if self.pickleversion is None or self.pickleversion == 'default':
                pickleversion = None
            elif self.pickleversion == 'highest':
                pickleversion = p.HIGHEST_PROTOCOL
            else:
                pickleversion = self.pickleversion
            if self.deflate:
                def _encode(obj):
                    return compress(p.dumps(obj, pickleversion), 1)
            else:
                def _encode(obj):
                    return p.dumps(obj, pickleversion)
            self._encode = _encode
            if self.deflate:
                def _decode(data):
                    if data is None:
                        return None
                    elif isinstance(data, Exception):
                        raise data
                    else:
                        try:
                            return p.loads(decompress(data))
                        except zlib_error:
                            return p.loads(data)
            else:
                def _decode(data):
                    if data is None:
                        return None
                    elif isinstance(data, Exception):
                        raise data
                    else:
                        return p.loads(data)
            self._decode = _decode
        else:
            if self.deflate:
                def _encode(obj):
                    return compress(json.dumps(obj, default=encode_default).encode('utf-8'), 1)
                self._encode = _encode
                def _decode(data):
                    if data is None:
                        return None
                    elif isinstance(data, Exception):
                        raise data
                    else:
                        try:
                            data = decompress(data)
                        except zlib_error:
                            pass
                        if not isinstance(data, str) and isinstance(data, bytes):
                            data = data.decode('utf-8')
                        return json.loads(data, object_hook=decode_object)
                self._decode = _decode
            else:
                def _encode(obj):
                    return json.dumps(obj, default=encode_default).encode('utf-8')
                self._encode = _encode
                def _decode(data):
                    if data is None:
                        return None
                    elif isinstance(data, Exception):
                        raise data
                    elif not isinstance(data, str) and isinstance(data, bytes):
                        data = data.decode('utf-8')
                    return json.loads(data, object_hook=decode_object)
                self._decode = _decode                
        self.appendAPI(api(self.getclient),
                       api(self.get, self.apiroutine),
                       api(self.set, self.apiroutine),
                       api(self.delete, self.apiroutine),
                       api(self.mget, self.apiroutine),
                       api(self.mgetwithcache, self.apiroutine),
                       api(self.mset, self.apiroutine),
                       api(self.update, self.apiroutine),
                       api(self.mupdate, self.apiroutine),
                       api(self.updateall, self.apiroutine),
                       api(self.updateallwithtime, self.apiroutine),
                       api(self.listallkeys, self.apiroutine))

    def _client_class(self, config, protocol, vhost):
        db = getattr(config, 'db', None)
        def _create_client(url, protocol, scheduler = None, key = None, certificate = None, ca_certs = None, bindaddress = None):
            c = RedisClient(url, db, protocol)
            if key:
                c.key = key
            if certificate:
                c.certificate = certificate
            if ca_certs:
                c.ca_certs = ca_certs
            self._redis_clients[vhost] = c
            return c.make_connobj(self.apiroutine)
        return _create_client

    def getclient(self, vhost = ''):
        "Return a tuple of ``(redisclient, encoder, decoder)`` for specified vhost"
        return (self._redis_clients.get(vhost), self._encode, self._decode)

    async def get(self, key, timeout = None, vhost = ''):
        "Get value from key"
        c = self._redis_clients.get(vhost)
        if c is None:
            raise ValueError('vhost ' + repr(vhost) + ' is not defined')
        if timeout is not None:
            if timeout <= 0:
                r = await c.batch_execute(self.apiroutine, ('MULTI',), 
                                                            ('GET', key),
                                                            ('DEL', key),
                                                            ('EXEC',))
            else:
                r = await c.batch_execute(self.apiroutine, ('MULTI',),
                                                            ('GET', key),
                                                            ('PEXPIRE', key, int(timeout * 1000)),
                                                            ('EXEC',))
            r = r[3][0]
            if isinstance(r, Exception):
                raise r
            return self._decode(r)
        else:
            r = await c.execute_command(self.apiroutine, 'GET', key)
            return self._decode(r)

    async def set(self, key, value, timeout = None, vhost = ''):
        "Set value to key, with an optional timeout"
        c = self._redis_clients.get(vhost)
        if timeout is None:
            await c.execute_command(self.apiroutine, 'SET', key, self._encode(value))
        elif timeout <= 0:
            await c.execute_command(self.apiroutine, 'DEL', key)
        else:
            await c.execute_command(self.apiroutine, 'PSETEX', key, int(timeout * 1000), self._encode(value))

    async def delete(self, key, vhost = ''):
        "Delete a key from the storage"
        c = self._redis_clients.get(vhost)
        await c.execute_command(self.apiroutine, 'DEL', key)

    async def _mget(self, keys, vhost = ''):
        if not keys:
            return []
        c = self._redis_clients.get(vhost)
        return await c.execute_command(self.apiroutine, 'MGET', *keys)

    async def mget(self, keys, vhost = ''):
        "Get multiple values from multiple keys"
        result = await self._mget(keys, vhost)
        return [self._decode(r) for r in result]

    async def mgetwithcache(self, keys, vhost = '', cache = None):
        "Get multiple values, cached when possible"
        result = await self._mget(keys, vhost)
        if cache is None:
            cache = KVCache()
        def _decode_with_cache(key, cached, new_data):
            if cached:
                old_data, decode_value = cached
                if old_data == new_data:
                    return decode_value, None
                else:
                    decode_value = self._decode(new_data)
                    return decode_value, (new_data, decode_value)
            else:
                decode_value = self._decode(new_data)
                return decode_value, (new_data, decode_value)
        return ([cache.update(k, _decode_with_cache, r)
                 for k,r in izip(keys, result)],
                cache)

    async def mset(self, kvpairs, timeout = None, vhost = ''):
        "Set multiple values on multiple keys"
        if not kvpairs:
            return
        c = self._redis_clients.get(vhost)
        d = kvpairs
        if hasattr(d, 'items'):
            d = d.items()
        if timeout is not None and timeout <= 0:
            await c.execute_command(self.apiroutine, 'DEL', *[k for k,_ in d])
        else:
            if timeout is None:
                await c.execute_command(self.apiroutine, 'MSET',
                                           *list(
                                               itertools.chain.from_iterable(
                                                   (k, self._encode(v)) for (k,v) in d
                                                )
                                            )
                                           )
            else:
                # Use a transact
                ptimeout = int(timeout * 1000)
                
                await c.batch_execute(self.apiroutine,
                                         *(
                                             (
                                                 ('MULTI',),
                                                 ('MSET',) + \
                                                    tuple(itertools.chain.from_iterable(
                                                            (k, self._encode(v)) for (k,v) in d
                                                          )
                                                        )
                                              ) + \
                                              tuple(
                                                  ('PEXPIRE', k, ptimeout) for k, _ in d
                                              ) + \
                                              (
                                                  ('EXEC',),
                                              )
                                           )
                                        )

    async def _retry_write(self, process, vhost):
        c = self._redis_clients.get(vhost)
        # Always try once first
        while True:
            newconn = await c.get_connection(self.apiroutine)
            with newconn.context(self.apiroutine):
                try:
                    return await process(newconn)
                except RedisConnectionDown:
                    continue
                except RedisWriteConflictException:
                    break
        enterseq = self.enterseq
        enterlock = self.enterlock
        for i in range(0, self.maxretry):
            newconn = await c.get_connection(self.apiroutine)
            with newconn.context(self.apiroutine):
                if self._sequencial:
                    curr_time = time()
                    if self._sequencialsince + 1.0 < curr_time:
                        self._sequencial = False
                    else:
                        self._sequencialsince = curr_time
                if self._sequencial:
                    # First make all the conflicted updates in this process retry in sequence
                    l = Lock(self, self.scheduler)
                    async with l:
                        try:
                            return await process(newconn)
                        except RedisConnectionDown:
                            continue
                        except RedisWriteConflictException:
                            if i > enterseq and not self._sequencial:
                                self._sequencial = True
                                self._sequencialsince = time()
                            if i > enterlock:
                                try:
                                    # Maybe too many VLCP processes are trying to write the same Redis server
                                    # Set a special flag in Redis with very short expire time
                                    # If multiple VLCP processes tries to set the flag at the same time, some
                                    # will be blocked for a short time to leave time for the winner
                                    for i in range(0, 100):
                                        r = await newconn.execute_command(self.apiroutine,
                                                                         'SET', 'vlcp._reserved.redisdb.connwriteblock',
                                                                         '1', 'PX', '100', 'NX')
                                        if r is not None:
                                            break
                                        else:
                                            await self.apiroutine.wait_with_timeout(0.02)
                                except Exception:
                                    self._logger.warning('Exception raised on waiting for a lock, will ignore and continue', exc_info = True)
                                    await self.apiroutine.wait_with_timeout(0.1)
                else:
                    try:
                        return await process(newconn)
                    except RedisConnectionDown:
                        continue
                    except RedisWriteConflictException:
                        if i > enterseq and not self._sequencial:
                            self._sequencial = True
                            self._sequencialsince = time()
        raise RedisWriteConflictException('Transaction still fails after many retries')

    async def update(self, key, updater, timeout = None, vhost = ''):
        '''
        Update in-place with a custom function
        
        :param key: key to update
        
        :param updater: ``func(k,v)``, should return a new value to update, or return None to delete. The function
                        may be call more than once.
        
        :param timeout: new timeout
        
        :returns: the updated value, or None if deleted
        '''
        async def _process(newconn):
            r = await newconn.batch_execute(self.apiroutine, ('WATCH', key), ('GET', key),
                                            raise_first_exception=True)
            v = self._decode(r[1])
            try:
                v = updater(key, v)
                if v is not None:
                    ve = self._encode(v)
            except Exception as exc:
                await newconn.execute_command(self.apiroutine, 'UNWATCH')
                raise exc
            if timeout is not None and timeout <= 0 or v is None:
                set_command = ('DEL', key)
            elif timeout is None:
                set_command = ('SET', key, ve)
            else:
                set_command = ('PSETEX', key, int(timeout * 1000), ve)
            result = await newconn.batch_execute(self.apiroutine, ('MULTI',),
                                                                  set_command,
                                                                  ('EXEC',))
            r = result[2]
            if r is not None:
                # Succeeded
                return v
            else:
                raise RedisWriteConflictException
        return await self._retry_write(_process, vhost)

    async def mupdate(self, keys, updater, timeout = None, vhost = ''):
        "Update multiple keys in-place with a custom function, see update. Either all success, or all fail."
        if not keys:
            return []
        async def _process(newconn):
            _, values = await newconn.batch_execute(self.apiroutine, ('WATCH', *keys), ('MGET', *keys),
                                                    raise_first_exception=True)
            try:
                values = [updater(k, self._decode(v)) for k,v in izip(keys,values)]
                keys_deleted = [k for k,v in izip(keys,values) if v is None]
                values_encoded = [(k,self._encode(v)) for k,v in izip(keys,values) if v is not None]
            except Exception as exc:
                await newconn.execute_command(self.apiroutine, 'UNWATCH')
                raise exc
            if timeout is None:
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            elif timeout <= 0:
                set_commands = (('DEL',) + tuple(keys),)
            else:
                ptimeout = int(timeout * 1000)
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                    set_commands_list.extend(('PEXPIRE', k, ptimeout) for k,_ in values_encoded)
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            if not set_commands:
                await newconn.execute_command(self.apiroutine, 'UNWATCH')
                return values
            result = await newconn.batch_execute(self.apiroutine, *((('MULTI',),) + \
                                                            set_commands + \
                                                            (('EXEC',),)))
            r = result[-1]
            if r is not None:
                # Succeeded
                return values
            else:
                raise RedisWriteConflictException('Transaction still fails after many retries: keys=' + repr(keys))
        return await self._retry_write(_process, vhost)

    async def updateall(self, keys, updater, timeout = None, vhost = ''):
        """
        Update multiple keys in-place, with a function ``updater(keys, values)``
        which returns ``(updated_keys, updated_values)``.
        
        Either all success or all fail
        """
        async def _process(newconn):
            if keys:
                _, values = await newconn.batch_execute(self.apiroutine, ('WATCH', *keys), ('MGET', *keys),
                                                        raise_first_exception=True)
            else:
                values = []
            try:
                new_keys, new_values = updater(keys, [self._decode(v) for v in values])
                keys_deleted = [k for k,v in izip(new_keys, new_values) if v is None]
                values_encoded = [(k,self._encode(v)) for k,v in izip(new_keys, new_values) if v is not None]
            except Exception as exc:
                if keys:
                    await newconn.execute_command(self.apiroutine, 'UNWATCH')
                raise exc
            if timeout is None:
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            elif timeout <= 0:
                if new_keys:
                    set_commands = (('DEL',) + tuple(new_keys),)
                else:
                    set_commands = ()
            else:
                ptimeout = int(timeout * 1000)
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                    set_commands_list.extend(('PEXPIRE', k, ptimeout) for k,_ in values_encoded)
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            if not set_commands:
                await newconn.execute_command(self.apiroutine, 'UNWATCH')
                return values
            result = await newconn.batch_execute(self.apiroutine, *((('MULTI',),) + \
                                                            set_commands + \
                                                            (('EXEC',),)))
            r = result[-1]
            if r is not None:
                # Succeeded
                return (new_keys, new_values)
            else:
                raise RedisWriteConflictException('Transaction still fails after many retries: keys=' + repr(keys))
        return await self._retry_write(_process, vhost)

    async def updateallwithtime(self, keys, updater, timeout = None, vhost = ''):
        """
        Update multiple keys in-place, with a function ``updater(keys, values, timestamp)``
        which returns ``(updated_keys, updated_values)``.
        
        Either all success or all fail.
        
        Timestamp is a integer standing for current time in microseconds.
        """
        async def _process(newconn):
            if keys:
                _, values, time_tuple = await newconn.batch_execute(self.apiroutine, ('WATCH', *keys),
                                                                                    ('MGET',) + tuple(keys),
                                                                                    ('TIME',),
                                                                    raise_first_exception=True)
            else:
                time_tuple = await newconn.execute_command(self.apiroutine, 'TIME')
                values = []
            server_time = int(time_tuple[0]) * 1000000 + int(time_tuple[1])
            try:
                new_keys, new_values = updater(keys, [self._decode(v) for v in values], server_time)
                keys_deleted = [k for k,v in izip(new_keys, new_values) if v is None]
                values_encoded = [(k,self._encode(v)) for k,v in izip(new_keys, new_values) if v is not None]
            except Exception as exc:
                if keys:
                    await newconn.execute_command(self.apiroutine, 'UNWATCH')
                raise exc
            if timeout is None:
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            elif timeout <= 0:
                if new_keys:
                    set_commands = (('DEL',) + tuple(new_keys),)
                else:
                    set_commands = ()
            else:
                ptimeout = int(timeout * 1000)
                set_commands_list = []
                if values_encoded:
                    set_commands_list.append(('MSET',) + tuple(itertools.chain.from_iterable(values_encoded)))
                    set_commands_list.extend(('PEXPIRE', k, ptimeout) for k,_ in values_encoded)
                if keys_deleted:
                    set_commands_list.append(('DEL',) + tuple(keys_deleted))
                set_commands = tuple(set_commands_list)
            if not set_commands:
                await newconn.execute_command(self.apiroutine, 'UNWATCH')
                return values
            result = await newconn.batch_execute(self.apiroutine, *((('MULTI',),) + \
                                                            set_commands + \
                                                            (('EXEC',),)))
            r = result[-1]
            if r is not None:
                # Succeeded
                return (new_keys, new_values)
            else:
                raise RedisWriteConflictException('Transaction still fails after many retries: keys=' + repr(keys))
        return await self._retry_write(_process, vhost)

    async def listallkeys(self, vhost = ''):
        '''
        Return all keys in the KVDB. For management purpose.
        '''
        c = self._redis_clients.get(vhost)
        if c is None:
            raise ValueError('vhost ' + repr(vhost) + ' is not defined')
        return await c.execute_command(self.apiroutine, 'KEYS', '*')

