import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = end - start
        return result, execution_time
    return wrapper


@measure_time
def slow_function():
    time.sleep(0.5)
    return "done"


if __name__ == "__main__":
    value, exec_time = slow_function()
    print(value)
    print(exec_time)