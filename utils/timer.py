import time
from functools import wraps


class Timer:
    """
    Expert-level utility for performance profiling.
    Can be used as a context manager or a decorator.
    """

    def __init__(self, name="Process"):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
        print(f"[TIMER] {self.name}: {self.interval:.4f} seconds")


def time_it(func):
    """Decorator to time a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {func.__name__}: {end - start:.4f} seconds")
        return result

    return wrapper
