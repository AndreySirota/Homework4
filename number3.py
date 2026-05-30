"""Test #2: number3"""


def s_numbers(x):
    """function for sum of numbers"""
    s = 0
    for i in range(1, x+1):
        s += i
    return s


number = int(input("Enter a number: "))
print(s_numbers(number))
