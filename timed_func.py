
import time

def timed_func(func_to_time):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return wrapper

