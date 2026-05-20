"""Homework 8: level_up"""


def main():
    """Execute homework task."""
    a = 3
    b = 8

    if a <= b and (a-b) % 2 == 0:
        print(f"solution({a}, {b}) = false")
    else:
        print(f"solution({a}, {b}) = true")


if __name__ == '__main__':
    main()
