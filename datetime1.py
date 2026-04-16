"""Homework 14: datetime1"""


from datetime import datetime


def main():
    """function main"""
    date1 = input()
    date2 = input()
    date_1 = datetime.strptime(date1, "%Y-%m-%d").date()
    date_2 = datetime.strptime(date2, "%Y-%m-%d").date()
    result = abs(date_2 - date_1).days
    print(result)


if __name__ == "__main__":
    main()
