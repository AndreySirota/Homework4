"""Homework 11: positive_arguments_of_function"""


def validate_arguments(func):
    """Execute homework task."""
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError(f"Arg {arg} isn't a positive number")
        for i, value in kwargs.items():
            if value <= 0:
                raise ValueError(f"Arg {i} = {value} isn't a positive number")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def rectangle_area(width, height):
    """Execute homework task."""
    return width * height


# print(rectangle_area(1, 2))

try:
    print(rectangle_area(-50, 100))
except ValueError as e:
    print(e)
