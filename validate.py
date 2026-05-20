"""Homework 9: validate"""


def solution(number):
    """Execute homework task."""
    list_number = list(str(number)[::-1])
    number_sum = 0
    list_number2 = list(map(int, list_number))

    for i, value in enumerate(list_number2):
        if i % 2 == 1:
            value *= 2
        if value > 9:
            value = value // 10 + value % 10
        number_sum += value
        list_number2[i] = value

    return bool(number_sum % 10 == 0)


print(solution(4561261212345467))
