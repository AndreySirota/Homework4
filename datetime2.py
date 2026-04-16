"""Homework 14: datetime2"""


from datetime import datetime, date


def main():
    """function main"""
    date1 = input()
    date_1 = datetime.strptime(date1, "%Y-%m-%d").date()
    data_2 = date.today()

    if data_2 < date_1:
        print("date entered is in the future.")
    elif data_2 > date_1:
        print("date entered is in the past.")
    else:
        print("dates match.")


if __name__ == "__main__":
    main()
