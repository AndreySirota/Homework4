"""Test #2: number4"""


def list_function(number):
    """function for list"""
    list_result = []
    number += 1
    while number > 0:
        list_result.append(number % 10)
        number = number // 10
    list_result.reverse()
    return list_result


test_number = int(input("Enter a number: "))
print(list_function(test_number))
