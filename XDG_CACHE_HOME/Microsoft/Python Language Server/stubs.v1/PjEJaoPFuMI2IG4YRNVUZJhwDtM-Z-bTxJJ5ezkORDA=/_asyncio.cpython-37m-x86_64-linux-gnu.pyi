class WeakSet(object):
    def __and__(self, other):
        return WeakSet()
    
    __class__ = WeakSet
    def __contains__(self, item):
        return False
    
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __ge__(self, other):
        return False
    
    def __gt__(self, other):
        return False
    
    __hash__ = None
    def __iand__(self, other):
        return None
    
    def __init__(self, data):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __ior__(self, other):
        return None
    
    def __isub__(self, other):
        return None
    
    def __iter__(self):
        return WeakSet()
    
    def __ixor__(self, other):
        return None
    
    def __le__(self, other):
        return False
    
    def __len__(self):
        return 0
    
    def __lt__(self, other):
        return False
    
    __module__ = '_weakrefset'
    def __or__(self, other):
        return WeakSet()
    
    def __reduce__(self):
        return ''; return ()
    
    def __sub__(self, other):
        return WeakSet()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def __xor__(self, other):
        return WeakSet()
    
    def _commit_removals(self):
        pass
    
    def add(self, item):
        pass
    
    def clear(self):
        pass
    
    def copy(self):
        pass
    
    def difference(self, other):
        pass
    
    def difference_update(self, other):
        pass
    
    def discard(self, item):
        pass
    
    def intersection(self, other):
        pass
    
    def intersection_update(self, other):
        pass
    
    def isdisjoint(self, other):
        pass
    
    def issubset(self, other):
        pass
    
    def issuperset(self, other):
        pass
    
    def pop(self):
        pass
    
    def remove(self, item):
        pass
    
    def symmetric_difference(self, other):
        pass
    
    def symmetric_difference_update(self, other):
        pass
    
    def union(self, other):
        pass
    
    def update(self, other):
        pass
    

class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if the dictionary has the specified key, else False.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, iterable):
        "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return dict()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Create a new dictionary with keys from iterable and values set to value.'
        pass
    
    def get(self, key, default):
        'Return the value for key if key is in the dictionary, else default.'
        pass
    
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        return tuple()
    
    def setdefault(self, key, default):
        'Insert key with a value of default if key is not in the dictionary.\n\nReturn the value for key if key is in the dictionary, else default.'
        pass
    
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
    

class Future(object):
    "This class is *almost* compatible with concurrent.futures.Future.\n\n    Differences:\n\n    - result() and exception() do not take a timeout argument and\n      raise an exception when the future isn't done yet.\n\n    - Callbacks registered with add_done_callback() are always called\n      via the event loop's call_soon_threadsafe().\n\n    - This class is not compatible with the wait() and as_completed()\n      methods in the concurrent.futures package."
    def __await__(self):
        'Return an iterator to be used in await expression.'
        pass
    
    __class__ = Future
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        "This class is *almost* compatible with concurrent.futures.Future.\n\n    Differences:\n\n    - result() and exception() do not take a timeout argument and\n      raise an exception when the future isn't done yet.\n\n    - Callbacks registered with add_done_callback() are always called\n      via the event loop's call_soon_threadsafe().\n\n    - This class is not compatible with the wait() and as_completed()\n      methods in the concurrent.futures package."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Future()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _asyncio_future_blocking(self):
        pass
    
    @property
    def _callbacks(self):
        pass
    
    @property
    def _exception(self):
        pass
    
    @property
    def _log_traceback(self):
        pass
    
    @property
    def _loop(self):
        pass
    
    def _repr_info(self):
        pass
    
    @property
    def _result(self):
        pass
    
    @property
    def _source_traceback(self):
        pass
    
    @property
    def _state(self):
        pass
    
    def add_done_callback(self, fn):
        'Add a callback to be run when the future becomes done.\n\nThe callback is called with a single argument - the future object. If\nthe future is already done when this is called, the callback is\nscheduled with call_soon.'
        pass
    
    def cancel(self):
        "Cancel the future and schedule callbacks.\n\nIf the future is already done or cancelled, return False.  Otherwise,\nchange the future's state to cancelled, schedule the callbacks and\nreturn True."
        pass
    
    def cancelled(self):
        'Return True if the future was cancelled.'
        pass
    
    def done(self):
        'Return True if the future is done.\n\nDone means either that a result / exception are available, or that the\nfuture was cancelled.'
        pass
    
    def exception(self):
        "Return the exception that was set on this future.\n\nThe exception (or None if no exception was set) is returned only if\nthe future is done.  If the future has been cancelled, raises\nCancelledError.  If the future isn't done yet, raises\nInvalidStateError."
        pass
    
    def get_loop(self):
        'Return the event loop the Future is bound to.'
        pass
    
    def remove_done_callback(self, fn):
        'Remove all instances of a callback from the "call when done" list.\n\nReturns the number of callbacks removed.'
        pass
    
    def result(self):
        "Return the result this future represents.\n\nIf the future has been cancelled, raises CancelledError.  If the\nfuture's result isn't yet available, raises InvalidStateError.  If\nthe future is done and has an exception set, this exception is raised."
        pass
    
    def set_exception(self, exception):
        'Mark the future done and set an exception.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    
    def set_result(self, result):
        'Mark the future done and set its result.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    

class Task(Future):
    'A coroutine wrapped in a Future.'
    def __await__(self):
        'Return an iterator to be used in await expression.'
        pass
    
    __class__ = Task
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        'A coroutine wrapped in a Future.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Task()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _asyncio_future_blocking(self):
        pass
    
    @property
    def _callbacks(self):
        pass
    
    @property
    def _coro(self):
        pass
    
    @property
    def _exception(self):
        pass
    
    @property
    def _fut_waiter(self):
        pass
    
    @property
    def _log_destroy_pending(self):
        pass
    
    @property
    def _log_traceback(self):
        pass
    
    @property
    def _loop(self):
        pass
    
    @property
    def _must_cancel(self):
        pass
    
    def _repr_info(self):
        pass
    
    @property
    def _result(self):
        pass
    
    @property
    def _source_traceback(self):
        pass
    
    @property
    def _state(self):
        pass
    
    def add_done_callback(self, fn):
        'Add a callback to be run when the future becomes done.\n\nThe callback is called with a single argument - the future object. If\nthe future is already done when this is called, the callback is\nscheduled with call_soon.'
        pass
    
    @classmethod
    def all_tasks(cls, type, loop):
        'Return a set of all tasks for an event loop.\n\nBy default all tasks for the current event loop are returned.'
        pass
    
    def cancel(self):
        'Request that this task cancel itself.\n\nThis arranges for a CancelledError to be thrown into the\nwrapped coroutine on the next cycle through the event loop.\nThe coroutine then has a chance to clean up or even deny\nthe request using try/except/finally.\n\nUnlike Future.cancel, this does not guarantee that the\ntask will be cancelled: the exception might be caught and\nacted upon, delaying cancellation of the task or preventing\ncancellation completely.  The task may also return a value or\nraise a different exception.\n\nImmediately after this method is called, Task.cancelled() will\nnot return True (unless the task was already cancelled).  A\ntask will be marked as cancelled when the wrapped coroutine\nterminates with a CancelledError exception (even if cancel()\nwas not called).'
        pass
    
    def cancelled(self):
        'Return True if the future was cancelled.'
        pass
    
    @classmethod
    def current_task(cls, type, loop):
        'Return the currently running task in an event loop or None.\n\nBy default the current task for the current event loop is returned.\n\nNone is returned when called not in the context of a Task.'
        pass
    
    def done(self):
        'Return True if the future is done.\n\nDone means either that a result / exception are available, or that the\nfuture was cancelled.'
        pass
    
    def exception(self):
        "Return the exception that was set on this future.\n\nThe exception (or None if no exception was set) is returned only if\nthe future is done.  If the future has been cancelled, raises\nCancelledError.  If the future isn't done yet, raises\nInvalidStateError."
        pass
    
    def get_stack(self):
        "Return the list of stack frames for this task's coroutine.\n\nIf the coroutine is not done, this returns the stack where it is\nsuspended.  If the coroutine has completed successfully or was\ncancelled, this returns an empty list.  If the coroutine was\nterminated by an exception, this returns the list of traceback\nframes.\n\nThe frames are always ordered from oldest to newest.\n\nThe optional limit gives the maximum number of frames to\nreturn; by default all available frames are returned.  Its\nmeaning differs depending on whether a stack or a traceback is\nreturned: the newest frames of a stack are returned, but the\noldest frames of a traceback are returned.  (This matches the\nbehavior of the traceback module.)\n\nFor reasons beyond our control, only one stack frame is\nreturned for a suspended coroutine."
        pass
    
    def print_stack(self):
        "Print the stack or traceback for this task's coroutine.\n\nThis produces output similar to that of the traceback module,\nfor the frames retrieved by get_stack().  The limit argument\nis passed to get_stack().  The file argument is an I/O stream\nto which the output is written; by default output is written\nto sys.stderr."
        pass
    
    def remove_done_callback(self, fn):
        'Remove all instances of a callback from the "call when done" list.\n\nReturns the number of callbacks removed.'
        pass
    
    def result(self):
        "Return the result this future represents.\n\nIf the future has been cancelled, raises CancelledError.  If the\nfuture's result isn't yet available, raises InvalidStateError.  If\nthe future is done and has an exception set, this exception is raised."
        pass
    
    def set_exception(self, exception):
        pass
    
    def set_result(self, result):
        pass
    

__doc__ = 'Accelerator module for asyncio'
__file__ = '/home/finoti/anaconda3/lib/python3.7/lib-dynload/_asyncio.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_asyncio'
__package__ = ''
_all_tasks = WeakSet()
_current_tasks = dict()
def _enter_task(loop, task):
    'Enter into task execution or resume suspended task.\n\nTask belongs to loop.\n\nReturns None.'
    pass

def _get_running_loop():
    'Return the running event loop or None.\n\nThis is a low-level function intended to be used by event loops.\nThis function is thread-specific.'
    pass

def _leave_task(loop, task):
    'Leave task execution or suspend a task.\n\nTask belongs to loop.\n\nReturns None.'
    pass

def _register_task(task):
    'Register a new task in asyncio as executed by loop.\n\nReturns None.'
    pass

def _set_running_loop(loop):
    'Set the running event loop.\n\nThis is a low-level function intended to be used by event loops.\nThis function is thread-specific.'
    pass

def _unregister_task(task):
    'Unregister a task.\n\nReturns None.'
    pass

def get_event_loop():
    'Return an asyncio event loop.\n\nWhen called from a coroutine or a callback (e.g. scheduled with\ncall_soon or similar API), this function will always return the\nrunning event loop.\n\nIf there is no running event loop set, the function will return\nthe result of `get_event_loop_policy().get_event_loop()` call.'
    pass

def get_running_loop():
    'Return the running event loop.  Raise a RuntimeError if there is none.\n\nThis function is thread-specific.'
    pass

