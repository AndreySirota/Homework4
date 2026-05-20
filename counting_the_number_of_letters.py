"""Homework 10: counting_the_number_of_letters"""


def solution(text):
    """Execute homework task."""
    list_text = list(text)
    result = []
    current_char = list_text[0]
    count = 1
    for value in list_text[1:]:
        if current_char == value:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_char}{count}")
            else:
                result.append(current_char)
            current_char = value
            count = 1
    if count > 1:
        result.append(f"{current_char}{count}")
    else:
        result.append(current_char)
    return "".join(result)


print(solution("aaabbdefffff"))
