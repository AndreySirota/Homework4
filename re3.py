"""Homework 14: re3"""


import re


def fix_repeat_words(text):
    """fix repeat words"""
    pattern = r'(\S+)(?:\s+\1)+'
    return re.sub(pattern, r'\1', text)


print(fix_repeat_words("Довольно распространённая ошибка "
                       "ошибка — это лишний повтор повтор слова"
                       " слова. Смешно, не не правда ли? Не"
                       " нужно портить хор хоровод"))
