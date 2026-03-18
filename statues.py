"""Homework 8: statues"""


def main():
    """Execute homework task."""
    list1 = [6, 2, 3, 8]
    min_list1 = min(list1)
    max_list1 = max(list1)
    count = 0
    x = min_list1

    for x in range(min_list1, max_list1+1):
        if x not in list1:
            count += 1
    print("Number of missing statues:", count)


if __name__ == '__main__':
    main()
