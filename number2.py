"""Test #2: number2"""


def number(n):
    """First function"""
    return n ** 2


def number2(n):
    """Second function"""
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")


x = int(input())
y = int(input())
print(number(x))
number2(y)
