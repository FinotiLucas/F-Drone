import builtins as _mod_builtins

class Empty(_mod_builtins.Exception):
    'Exception raised by Queue.get(block=0)/get_nowait().'
    __class__ = Empty
    __dict__ = {}
    def __init__(self, block=0):
        'Exception raised by Queue.get(block=0)/get_nowait().'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_queue'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class SimpleQueue(_mod_builtins.object):
    'Simple, unbounded, reentrant FIFO queue.'
    __class__ = SimpleQueue
    def __init__(self, *args, **kwargs):
        'Simple, unbounded, reentrant FIFO queue.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def empty(self):
        'Return True if the queue is empty, False otherwise (not reliable!).'
        pass
    
    def get(self, block, timeout):
        "Remove and return an item from the queue.\n\nIf optional args 'block' is true and 'timeout' is None (the default),\nblock if necessary until an item is available. If 'timeout' is\na non-negative number, it blocks at most 'timeout' seconds and raises\nthe Empty exception if no item was available within that time.\nOtherwise ('block' is false), return an item if one is immediately\navailable, else raise the Empty exception ('timeout' is ignored\nin that case)."
        pass
    
    def get_nowait(self):
        'Remove and return an item from the queue without blocking.\n\nOnly get an item if one is immediately available. Otherwise\nraise the Empty exception.'
        pass
    
    def put(self, item, block, timeout):
        "Put the item on the queue.\n\nThe optional 'block' and 'timeout' arguments are ignored, as this method\nnever blocks.  They are provided for compatibility with the Queue class."
        pass
    
    def put_nowait(self, item):
        'Put an item into the queue without blocking.\n\nThis is exactly equivalent to `put(item)` and is only provided\nfor compatibility with the Queue class.'
        pass
    
    def qsize(self):
        'Return the approximate size of the queue (not reliable!).'
        pass
    

__doc__ = 'C implementation of the Python queue module.\nThis module is an implementation detail, please do not use it directly.'
__file__ = '/home/finoti/anaconda3/lib/python3.7/lib-dynload/_queue.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_queue'
__package__ = ''
