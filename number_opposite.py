"""Homework 9: number_opposite"""


def solution(n, first_number):
    """Execute homework task."""
    half_degrees = n // 2
    if n % 2 == 0:
        if first_number < half_degrees:
            return first_number + half_degrees
        return first_number - half_degrees
    return "Число не соответствуeт условию задачи"


print(solution(14, 7))
