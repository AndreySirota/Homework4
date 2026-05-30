"""Homework 7: level_up"""


def main():
    """Execute homework task."""
    experience = int(input())
    threshold = int(input())
    reward = int(input())

    if (experience + reward) >= threshold:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
