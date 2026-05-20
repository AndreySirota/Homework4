"""Test #2: number7"""


def f(s, number):
    """function f"""
    list_s = []
    list_result = []
    for i, char in enumerate(s):
        list_s.append(char)
        if i == number - 1:
            break
    result = "".join(list_s)
    reverse_result = result[::-1]
    for i in range(1, len(reverse_result)):
        list_result.append(reverse_result[i])
    final_result = result + "".join(list_result)
    return final_result


MESSAGE = "abcdefghijklmnopqrstuvwxyz"
print(f(MESSAGE, 10))
