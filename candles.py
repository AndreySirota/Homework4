"""Homework 10: candles"""


def solution(candle_number, make_new):
    """Execute homework task."""
    k = 1 / make_new
    candle_sum = 0
    candle_number_sum_mod = 0
    while candle_number > 0:
        candle_sum += candle_number
        candle_number = candle_number * k
        candle_number_mod = candle_number - int(candle_number)
        candle_number_sum_mod += candle_number_mod
        if candle_number_sum_mod >= 1:
            candle_number += 1
            candle_number_sum_mod -= 1
        candle_number = int(candle_number)
    return candle_sum


print(solution(2, 3))
