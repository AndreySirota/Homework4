"""Homework 14: re1"""


import re


def find_dates(file):
    """function find_dates"""
    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    dates = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                found = re.findall(pattern, line)
                dates.extend(found)
    except FileNotFoundError:
        print(f"File {file} not found. ")
    return dates


def main():
    """function main"""
    file = input().strip()
    dates = find_dates(file)
    if dates:
        for date in dates:
            print(date)
    else:
        print("No dates found. ")


if __name__ == "__main__":
    main()
