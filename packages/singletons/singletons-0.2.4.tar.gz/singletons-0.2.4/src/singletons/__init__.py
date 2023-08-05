__version__ = '__version__ = '0.2.4''

from .factory import EventletFactory, GeventFactory, GlobalFactory, GreenthreadFactory, ProcessFactory, ThreadFactory
from .singleton import EventletSingleton, GeventSingleton, GreenthreadSingleton, ProcessSingleton, Singleton, \
    ThreadSingleton
from .utils import detect_greenthread_environment
from .shared_module import SharedModule

__all__ = [
    'EventletFactory', 'GeventFactory', 'GlobalFactory', 'GreenthreadFactory', 'ProcessFactory', 'ThreadFactory',
    'EventletSingleton', 'GeventSingleton', 'GreenthreadSingleton', 'ProcessSingleton', 'Singleton', 'ThreadSingleton',
    'detect_greenthread_environment',
    'SharedModule',
]
