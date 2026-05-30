"""Homework 9: sequence"""


def solution(sequence):
    """Execute homework task."""
    result_sequence = sequence[:]
    for i in range(1, len(result_sequence)):
        if result_sequence[i] <= result_sequence[i-1]:
            del result_sequence[i]
            break

    for i in range(1, len(result_sequence)):
        if result_sequence[i] <= result_sequence[i-1]:
            return False
    return True


print(solution([1, 2, 1, 3]))
