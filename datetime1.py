"""Homework 14: datetime1"""


from datetime import datetime


def get_date():
    """function get_date"""
    date = input()
    return datetime.strptime(date, "%Y-%m-%d").date()


def number_of_days():
    """function number_of_days"""
    start_date = get_date()
    end_date = get_date()
    diff = abs(end_date - start_date).days
    print(f"The difference between {start_date} and {end_date} is {diff}")


number_of_days()
