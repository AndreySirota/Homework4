"""Homework 14: re2"""


import re


def is_valid_password(password):
    """function is_valid_password"""
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))


def validate_user_password():
    """function validate_user_password"""
    password = input()
    if is_valid_password(password):
        print("password correct")
    else:
        print("password incorrect")


validate_user_password()
