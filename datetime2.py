"""Homework 14: datetime2"""


from datetime import datetime, date


def get_date():
    """function get_date"""
    date1 = input()
    return datetime.strptime(date1, "%Y-%m-%d").date()


def is_date_of_future_or_past():
    """function is_date_of_future_or_past"""
    input_date = get_date()
    current_date = date.today()

    if current_date < input_date:
        print("date entered is in the future.")
    elif current_date > input_date:
        print("date entered is in the past.")
    else:
        print("dates match.")


is_date_of_future_or_past()
