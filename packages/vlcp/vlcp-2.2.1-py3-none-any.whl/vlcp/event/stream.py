'''
Created on 2015/8/14

:author: hubo
'''

from vlcp.event import Event, withIndices
import os

@withIndices('stream', 'type')
class StreamDataEvent(Event):
    canignore = False
    STREAM_DATA = 'data'
    STREAM_EOF = 'eof'
    STREAM_ERROR = 'error'
    def canignorenow(self):
        return self.stream.closed

class BaseStream(object):
    "Streaming base"
    def __init__(self, isunicode = False, encoders = []):
        '''
        Constructor
        
        :param isunicode: if True, the data used in this stream outputs unicode string. Otherwise it outputs bytes.
        
        :param encoders: a list of functions `enc(data, is_eof)` which encodes input data.
        '''
        self.data = b''
        self.pos = 0
        self.dataeof = False
        self.dataerror = False
        self.eof = False
        self.errored = False
        self.closed = False
        self.writeclosed = False
        self.allowwrite = False
        self.isunicode = isunicode
        self.encoders = list(encoders)
    def getEncoderList(self):
        """
        Return the encoder list
        """
        return self.encoders
    def _parsedata(self, data, dataeof, dataerror):
        self.pos = 0
        self.dataeof = dataeof
        self.dataerror = dataerror
        if len(data) > 0 or self.dataeof:
            for enc in self.encoders:
                try:
                    data = enc(data, self.dataeof)
                except:
                    self.errored = True
                    self.closed = True
                    raise
        self.data = data
    async def read(self, container = None, size = None):
        """
        Coroutine method to read from the stream and return the data. Raises EOFError
        when the stream end has been reached; raises IOError if there are other errors.
        
        :param container: A routine container
        
        :param size: maximum read size, or unlimited if is None
        """
        ret = []
        retsize = 0
        if self.eof:
            raise EOFError
        if self.errored:
            raise IOError('Stream is broken before EOF')
        while size is None or retsize < size:
            if self.pos >= len(self.data):
                await self.prepareRead(container)
            if size is None or size - retsize >= len(self.data) - self.pos:
                t = self.data[self.pos:]
                ret.append(t)
                retsize += len(t)
                self.pos = len(self.data)
                if self.dataeof:
                    self.eof = True
                    break
                if self.dataerror:
                    self.errored = True
                    break
            else:
                ret.append(self.data[self.pos:self.pos + (size - retsize)])
                self.pos += (size - retsize)
                retsize = size
                break
        if self.isunicode:
            return u''.join(ret)
        else:
            return b''.join(ret)
        if self.errored:
            raise IOError('Stream is broken before EOF')
    def readonce(self, size = None):
        """
        Read from current buffer. If current buffer is empty, returns an empty string. You can use `prepareRead`
        to read the next chunk of data.
        
        This is not a coroutine method.
        """
        if self.eof:
            raise EOFError
        if self.errored:
            raise IOError('Stream is broken before EOF')
        if size is not None and size < len(self.data) - self.pos:
            ret = self.data[self.pos: self.pos + size]
            self.pos += size
            return ret
        else:
            ret = self.data[self.pos:]
            self.pos = len(self.data)
            if self.dataeof:
                self.eof = True
            return ret
    async def prepareRead(self, container = None):
        """
        A coroutine method to read the next chunk of data.
        """
        raise NotImplementedError
    
    async def readline(self, container = None, size = None):
        """
        Coroutine method which reads the next line or until EOF or size exceeds
        """
        ret = []
        retsize = 0
        if self.eof:
            raise EOFError
        if self.errored:
            raise IOError('Stream is broken before EOF')
        while size is None or retsize < size:
            if self.pos >= len(self.data):
                await self.prepareRead(container)
            if size is None or size - retsize >= len(self.data) - self.pos:
                t = self.data[self.pos:]
                if self.isunicode:
                    p = t.find(u'\n')
                else:
                    p = t.find(b'\n')
                if p >= 0:
                    t = t[0: p + 1]
                    ret.append(t)
                    retsize += len(t)
                    self.pos += len(t)
                    break
                else:
                    ret.append(t)
                    retsize += len(t)
                    self.pos += len(t)
                    if self.dataeof:
                        self.eof = True
                        break
                    if self.dataerror:
                        self.errored = True
                        break
            else:
                t = self.data[self.pos:self.pos + (size - retsize)]
                if self.isunicode:
                    p = t.find(u'\n')
                else:
                    p = t.find(b'\n')
                if p >= 0:
                    t = t[0: p + 1]
                ret.append(t)
                self.pos += len(t)
                retsize += len(t)
                break
        if self.isunicode:
            return u''.join(ret)
        else:
            return b''.join(ret)
        if self.errored:
            raise IOError('Stream is broken before EOF')
    async def copy_to(self, dest, container, buffering = True):
        """
        Coroutine method to copy content from this stream to another stream.
        """
        if self.eof:
            await dest.write(u'' if self.isunicode else b'', True)
        elif self.errored:
            await dest.error(container)
        else:
            try:
                while not self.eof:
                    await self.prepareRead(container)
                    data = self.readonce()
                    try:
                        await dest.write(data, container, self.eof, buffering = buffering)
                    except IOError:
                        break
            except:
                async def _cleanup():
                    try:
                        await dest.error(container)
                    except IOError:
                        pass
                container.subroutine(_cleanup(), False)
                raise
            finally:
                self.close(container.scheduler)

    copyTo = copy_to

    async def write(self, data, container, eof = False, ignoreexception = False, buffering = True, split = True):
        """
        Coroutine method to write data to this stream.
        
        :param data: data to write
        
        :param container: the routine container
        
        :param eof: if True, this is the last chunk of this stream. The other end will receive an EOF after reading
                    this chunk.
                    
        :param ignoreexception: even if the stream is closed on the other side, do not raise exception.
        
        :param buffering: enable buffering. The written data may not be sent if buffering = True; if buffering = False,
                          immediately send any data in the buffer together with this chunk.
        
        :param split: enable splitting. If this chunk is too large, the stream is allowed to split it into
                      smaller chunks for better balancing.
        """
        if not ignoreexception:
            raise IOError('Stream is closed')

    async def error(self, container, ignoreexception = False):
        """
        Raises error on this stream, so that the receiving end gets an IOError exception.
        """
        if not ignoreexception:
            raise IOError('Stream is closed')

    def close(self, scheduler, allowwrite = False):
        """
        Read side close. To close at the write side, use `eof=True` with `write`.
        
        :param scheduler: the scheduler
        
        :param allowwrite: do not raise exception on the write side
        """
        self.closed = True

class Stream(BaseStream):
    '''
    Streaming data with events
    '''
    def __init__(self, isunicode = False, encoders = [], writebufferlimit = 4096, splitsize = 1048576):
        '''
        Constructor
        
        :param isunicode: True if this stream outputs unicode; False if this stream outputs bytes
        
        :param encoders: a list of functions `enc(data, is_eof)` which encodes input data.
        
        :param writebufferlimit: if `buffering=True` on `write`, do not send data until there is more data than this limit
                                 
        :param splitsize: if `split=True` on `write`, split chunks larger than this to chunks with this size
        '''
        BaseStream.__init__(self, isunicode, encoders)
        self.dm = StreamDataEvent.createMatcher(self, None)
        self.writebuffer = []
        self.writebuffersize = 0
        self.writebufferlimit = writebufferlimit
        self.splitsize = splitsize
    async def prepareRead(self, container = None):
        if not self.eof and not self.errored and self.pos >= len(self.data):
            ev = await self.dm
            ev.canignore = True
            self._parsedata(ev.data, ev.type == StreamDataEvent.STREAM_EOF,
                            ev.type == StreamDataEvent.STREAM_ERROR)
    async def write(self, data, container, eof = False, ignoreexception = False, buffering = True, split = True):
        if self.closed or self.writeclosed:
            if not ignoreexception and not self.allowwrite:
                raise IOError('Stream is closed')
        else:
            if eof:
                buffering = False
            if buffering and self.writebufferlimit is not None and self.writebuffersize + len(data) > self.writebufferlimit:
                buffering = False
            if buffering:
                self.writebuffer.append(data)
                self.writebuffersize += len(data)
            else:
                data = data[0:0].join(self.writebuffer) + data
                if not data:
                    split = False
                del self.writebuffer[:]
                self.writebuffersize = 0
                if split:
                    for i in range(0, len(data), self.splitsize):
                        await container.wait_for_send(StreamDataEvent(self,
                                                                       StreamDataEvent.STREAM_EOF if eof and i + self.splitsize >= len(data) else StreamDataEvent.STREAM_DATA,
                                                                       data = data[i : i + self.splitsize]))
                else:
                    await container.waitForSend(StreamDataEvent(self,
                                                                   StreamDataEvent.STREAM_EOF if eof else StreamDataEvent.STREAM_DATA,
                                                                   data = data))
                if eof:
                    self.writeclosed = True
    async def error(self, container, ignoreexception = False):
        if self.closed or self.writeclosed:
            if not ignoreexception and not self.allowwrite:
                raise IOError('Stream is closed')
        else:
            await container.waitForSend(StreamDataEvent(self, StreamDataEvent.STREAM_ERROR, data = b''))
            self.writeclosed = True
    def close(self, scheduler, allowwrite = False):
        self.closed = True
        self.allowwrite = allowwrite
        scheduler.ignore(self.dm)

class MemoryStream(BaseStream):
    '''
    A stream with readonly data
    '''
    def __init__(self, data, encoders= [], isunicode = None):
        '''
        Constructor
        
        :param data: all input data
        
        :param encoders: encoder list
        
        :param isunicode: Whether this stream outputs unicode. Default to be the same to data. Notice that
                          the encoders may change bytes data to unicode or vice-versa
        '''
        BaseStream.__init__(self, not isinstance(data, bytes) if isunicode is None else isunicode, encoders)
        self.preloaddata = data
    def __len__(self):
        return len(self.preloaddata)
    async def prepareRead(self, container = None):
        if not self.eof and not self.errored and self.pos >= len(self.data):
            self._parsedata(self.preloaddata, True, False)

class FileStream(BaseStream):
    "A stream from a file-like object. The file-like object must be in blocking mode"
    def __init__(self, fobj, encoders = [], isunicode = None, size = None, readlimit = 65536):
        "Constructor"
        if isunicode is None:
            mode = getattr(fobj, 'mode', 'rb')
            if 'b' in mode:
                isunicode = False
            elif str is bytes:
                isunicode = False
            else:
                isunicode = True
        BaseStream.__init__(self, isunicode, encoders)
        self.fobj = fobj
        self.size = None
        try:
            self.size = os.fstat(fobj.fileno()).st_size
            self.size -= fobj.tell()
            if self.size > size:
                self.size = size
        except Exception:
            if size:
                self.size = size
        self.readlimit = readlimit
        self.totalbuffered = 0
    def __len__(self):
        if self.size is None:
            raise TypeError('Cannot determine file size')
        else:
            return self.size
    async def prepareRead(self, container = None):
        if not self.eof and not self.errored and self.pos >= len(self.data):
            try:
                readlimit = self.readlimit
                if self.size is not None and self.size - self.totalbuffered < readlimit:
                    readlimit = self.size - self.totalbuffered 
                data = self.fobj.read(readlimit)
                self.totalbuffered += len(data)
                eof = not data
                if self.size is not None and self.totalbuffered >= self.size:
                    eof = True
            except Exception:
                self._parsedata(b'', False, True)
            else:
                self._parsedata(data, eof, False)

    def close(self, scheduler=None, allowwrite=False):
        self.fobj.close()
        BaseStream.close(self, scheduler=scheduler, allowwrite=allowwrite)

class FileWriter(object):
    "Write to file"
    def __init__(self, fobj):
        self.fobj = fobj

    async def write(self, data, container, eof = False, ignoreexception = False, buffering = True, split = True):
        try:
            if data:
                self.fobj.write(data)
            if eof:
                self.fobj.close()
        except Exception:
            if not ignoreexception:
                raise

    async def error(self, container, ignoreexception = False):
        try:
            self.fobj.close()
        except Exception:
            if not ignoreexception:
                raise
