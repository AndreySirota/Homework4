"""Test #2: number5"""


def is_palindrome(number):
    """palindrome function"""
    if number < 0:
        return False
    if number != 0 and number % 10 == 0:
        return False
    number2 = 0
    while number > number2:
        number2 = number2 * 10 + number % 10
        number = number // 10
    return number in (number2, number2 // 10)


test_number = int(input("Enter a number: "))
print(is_palindrome(test_number))
