from Performance_analyzer import Performance_analyzer as PA
from time import time

def proxy(analyzer: PA):
    def before(func):
        def wrapper(*args, **kw):
            key = hash(time())
            analyzer.before_service(key)
            result = func(*args, **kw)
            analyzer.after_service(key)
        return wrapper
    return before