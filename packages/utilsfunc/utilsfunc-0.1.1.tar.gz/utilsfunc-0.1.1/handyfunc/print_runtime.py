import time


def print_runtime(func):
    """Compute running time of function"""
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        runtime = round((time.time() - start_time), 3)
        print(f'current Function >>>{func.__name__}<<< run time is {runtime}')
    return wrapper


if __name__ == '__main__':
    import numpy as np

    @print_runtime
    def test_func():
        v = np.random.rand(100000)
        u = np.random.rand(100000)
        return np.dot(v, u)

    test_func()

