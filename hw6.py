"""Homework #6: string and list operations."""


def main():
    """Execute all homework tasks."""
    # 1
    message = "www.my_site.com#about"
    print(message.replace("#", "/"))

    # 2
    s1 = "eat"
    s2 = "drink"
    s3 = "swim"
    print(s1 + "ing")
    print(s2 + "ing")
    print(s3 + "ing")

    # 3
    txt = "Ivanou Ivan"
    print(txt[7:11] + " " + txt[0:6])

    # 4
    test_string = " one two three four "
    print(test_string.strip())

    # 5
    cities = "lONDON pARIS bERLIN mADRID"
    print(cities.title())

    # 6
    name_surname = "Robin Singh"
    txt_msg = "I love arrays they are my favorite"
    print(name_surname.split())
    print(txt_msg.split())

    # 7
    list_one = ["Robin Singh"]
    welcome = "Welcome"
    airport = "airport"
    print(f"Hello, {list_one[0]}! {welcome} to {airport}")

    # 8
    list_two = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    list_result = " ".join(list_two)
    print(list_result)

    # 9
    list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    list_numbers[2] = '30'
    list_numbers.pop(6)
    print(list_numbers)


if __name__ == '__main__':
    main()
