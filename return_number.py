"""Homework 11: return_number"""


def number(func):
    """Execute homework task."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (float, int)):
            print(f"{result} isn't a number")
        return result
    return wrapper


@number
def rectangle_area(width, height):
    """rectangle_area"""
    return width * height
