"""Homework 7: time_converter"""


def main():
    """Execute homework task."""
    n = int(input())
    h = n // 60
    m = n % 60
    a = h % 12
    c = m // 10
    d = m % 10

    str1 = ""
    if h >= 12:
        str1 = str(a + 12) + ":" + str(c) + str(d)
    elif 10 <= h < 12:
        str1 = str(a) + ":" + str(c) + str(d)
    elif h < 10:
        str1 = str(0) + str(a) + ":" + str(c) + str(d)

    if h == 12:
        str2 = str1 + " == " + str(a + 12) + ":" + str(c) + str(d) + " p.m."
        print(str2)
    elif h > 12:
        str3 = str1 + " == " + str(a) + ":" + str(c) + str(d) + " p.m."
        print(str3)
    elif 10 <= h < 12:
        str4 = str1 + " == " + str(a) + ":" + str(c) + str(d) + " a.m."
        print(str4)
    elif h == 0:
        str5 = str1 + " == " + str(a + 12) + ":" + str(c) + str(d) + " a.m."
        print(str5)
    elif h < 10:
        str6 = str1 + " == " + str(a) + ":" + str(c) + str(d) + " a.m."
        print(str6)


if __name__ == '__main__':
    main()
