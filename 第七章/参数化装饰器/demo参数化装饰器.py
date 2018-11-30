import functools
import time


def clock(param):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_str = ','.join(repr(arg) for arg in args)
            print('[%0.8fs] %s(%s)-> %r' % (elapsed, name, arg_str, result))
            print(param)
            return result
        return clocked
    return decorate


@clock('参数')
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


m = factorial(3)
print(m)
