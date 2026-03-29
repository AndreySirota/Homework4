"""Homework 11: cashing_function"""


def cache(func):
    """Execute homework task."""
    cache_storage = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_storage:
            cache_storage[key] = func(*args, **kwargs)
        return cache_storage[key]
    return wrapper


@cache
def fibonacci(n):
    """Execute homework task."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
