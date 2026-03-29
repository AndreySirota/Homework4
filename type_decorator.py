"""Homework 11: type_decorator"""


def typed(type_):
    """Execute homework task."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            a_num, b_num = args[0], args[1]
            if type_ is str:
                a_num, b_num = str(a_num), str(b_num)
            elif type_ is int:
                a_num, b_num = int(a_num), int(b_num)
            elif type_ is float:
                a_num, b_num = float(a_num), float(b_num)
            return func(a_num, b_num, *args[2:], **kwargs)
        return wrapper
    return decorator


@typed(type_=str)
def add(a, b):
    """Execute homework task."""
    return a + b


print(add("3", 5))
print(add(5, 5))
print(add('a', 'b'))
