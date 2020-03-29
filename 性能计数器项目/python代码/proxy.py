from time import time

def proxy(analyzer):
    def before(func):
        def wrapper(*args, **kw):
            key = hash(time())
            analyzer.before_service(key)
            result = func(*args, **kw)
            analyzer.after_service(key)
            return result
        return wrapper
    return before