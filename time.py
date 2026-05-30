"""Homework 7: time"""


def main():
    """Execute homework task."""
    n = int(input("Введите n = "))
    m = n // 60
    s = n % 60

    if 10 <= m < 100:
        a = m // 10
        b = m % 10
    else:
        a = 0
        b = m % 10

    if 10 <= s < 100:
        c = s // 10
        d = s % 10
    else:
        c = 0
        d = s % 10

    summa = a + b + c + d
    str1 = str(a) + str(b) + ":" + str(c) + str(d)
    print("Для n = ", n, ", результат должен быть: ", summa, sep="")
    print(n, "минут прошло, и это означает что сейчас", str1)


if __name__ == '__main__':
    main()
