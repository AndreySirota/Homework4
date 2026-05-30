"""Homework 8: bulls_and_cows"""


import random
import string


def main():
    """Execute homework task."""
    first = random.choice(string.digits[1:])
    second = random.sample(string.digits, 3)
    secret_number = first + "".join(second)
    a = int(secret_number) // 1000
    b = (int(secret_number) // 100) % 10
    c = (int(secret_number) // 10) % 10
    d = int(secret_number) % 10
    number = 0

    while secret_number != number:
        count_bull = 0
        count_cow = 0
        number = int(input("Enter your guess:\n> "))

        e = number // 1000
        f = (number // 100) % 10
        g = (number // 10) % 10
        h = number % 10

        if len({e, f, g, h}) == 4:
            if e == a:
                count_bull += 1
            if f == b:
                count_bull += 1
            if g == c:
                count_bull += 1
            if h == d:
                count_bull += 1
            if e in (b, c, d):
                count_cow += 1
            if f in (a, c, d):
                count_cow += 1
            if g in (a, b, d):
                count_cow += 1
            if h in (a, b, c):
                count_cow += 1
            if (count_cow == 0) and (count_bull == 4):
                print("Вы выиграли!")
                break
            print(f"{count_cow} коровы, {count_bull} бык")
        else:
            print("В числе есть повторяющиеся цифры")


if __name__ == '__main__':
    main()
