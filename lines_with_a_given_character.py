"""Homework 10: lines_with_a_given_character"""


def solution(text):
    """Execute homework task."""
    list_text = list(text)
    i = 0
    while i < len(list_text):
        if list_text[i] == "#":
            del list_text[i]
            if i > 0:
                del list_text[i-1]
                i = max(0, i - 2)
            else:
                i = max(0, i - 1)
        else:
            i += 1
        if "#" not in list_text:
            break
    return "".join(list_text)


print(solution("a#bc#d"))
