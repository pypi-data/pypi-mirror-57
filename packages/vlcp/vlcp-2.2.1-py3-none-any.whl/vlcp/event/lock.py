'''
Created on 2015/12/14

:author: hubo

Lock is created by limiting queue length of LockEvent, so there is only one event in the queue.
Other send request is blocked by the queue.
'''
from vlcp.event.event import Event, withIndices
from vlcp.event.pqueue import CBQueue
from vlcp.event.core import syscall_removequeue
from vlcp.event.runnable import RoutineContainer

@withIndices('context', 'key', 'locker')
class LockEvent(Event):
    canignore = False
    def canignorenow(self):
        return not self.locker.locked

@withIndices('locker', 'context', 'key')
class LockedEvent(Event):
    pass

class Lock(object):
    """
    An lock object. Normal usage::
        
        my_lock = Lock(lock_obj, container.scheduler)
        await my_lock.lock(container)
        with my_lock:
            ...
    
    Or use async with::
    
        async with my_lock:
            ...
    """
    def __init__(self, key, scheduler, context = 'default'):
        """
        Create a lock object. You do not need to share this object with other routines;
        all locks with the same *key* and *context* are mutual exclusive.
        
        :param key: Any hashable value.
        
        :param scheduler: The scheduler
        
        :param context: An extra object to separate keys into different context
        """
        self.key = key
        self.context = context
        self.scheduler = scheduler
        self.locked = False
        self.lockroutine = None
    async def lock(self, container = None):
        "Wait for lock acquire"
        if container is None:
            container = RoutineContainer.get_container(self.scheduler)
        if self.locked:
            pass
        elif self.lockroutine:
            await LockedEvent.createMatcher(self)
        else:
            await container.wait_for_send(LockEvent(self.context, self.key, self))
            self.locked = True
    def trylock(self):
        "Try to acquire lock and return True; if cannot acquire the lock at this moment, return False."
        if self.locked:
            return True
        if self.lockroutine:
            return False
        waiter = self.scheduler.send(LockEvent(self.context, self.key, self))
        if waiter:
            return False
        else:
            self.locked = True
            return True
    async def _lockroutine(self, container):
        await self.lock(container)
        await container.wait_for_send(LockedEvent(self, self.context, self.key))
    def beginlock(self, container):
        "Start to acquire lock in another routine. Call trylock or lock later to acquire the lock. Call unlock to cancel the lock routine"
        if self.locked:
            return True
        if self.lockroutine:
            return False
        self.lockroutine = container.subroutine(self._lockroutine(container), False)
        return self.locked
    def unlock(self):
        "Unlock the key"
        if self.lockroutine:
            self.lockroutine.close()
            self.lockroutine = None
        if self.locked:
            self.locked = False
            self.scheduler.ignore(LockEvent.createMatcher(self.context, self.key, self))
    def __del__(self):
        self.unlock()
    def __enter__(self):
        if not self.locked:
            raise ValueError('Not locked; must first acquire the lock, then use with...')
        return self
    def __exit__(self, exctype, excvalue, traceback):
        self.unlock()
        return False
    
    async def __aenter__(self):
        await self.lock()
        return self
    
    async def __aexit__(self, exctype, excvalue, traceback):
        self.unlock()
        return False

class Semaphore(object):
    """
    Change the default behavior of Lock for specified context and key from lock to semaphore. The default
    behavior of Lock allows only one routine for a specified key; when a semaphore is created, limited number
    of routines can retrieve the Lock at the same time.
    """
    def __init__(self, key, size, scheduler, context = 'default', priority = 1000):
        """
        Prepare to change locks on *key* and *context* to a semaphore.
        
        :param key: Hashable object used by locks.
        
        :param size: Semaphore size, which means the maximum allowed routines to retrieve the lock
                     at the same time
                     
        :param scheduler: The scheduler
        
        :param context: context object used by locks.
        
        :param priority: priority for the created queue.
        """
        self.context = context
        self.key = key
        self.scheduler = scheduler
        self.priority = priority
        self.size = size
        self.queue = None
    def create(self):
        """
        Create the subqueue to change the default behavior of Lock to semaphore.
        """
        self.queue = self.scheduler.queue.addSubQueue(self.priority, LockEvent.createMatcher(self.context, self.key),
                                         maxdefault = self.size, defaultQueueClass = CBQueue.AutoClassQueue.initHelper('locker', subqueuelimit = 1))
    async def destroy(self, container = None):
        """
        Destroy the created subqueue to change the behavior back to Lock
        """
        if container is None:
            container = RoutineContainer(self.scheduler)
        if self.queue is not None:
            await container.syscall_noreturn(syscall_removequeue(self.scheduler.queue, self.queue))
            self.queue = None
