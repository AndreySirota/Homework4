"""Test #2: number6"""


def read_file(file):
    """function for reading to file"""
    try:
        with open(file, "r", encoding='utf-8') as f:
            result = f.read()
        lines = result.count("\n") + 1
        words = len(result.split())
        chars = len(result)
        return {"lines": lines, "words": words, "chars": chars}
    except FileNotFoundError:
        print(f"File {file} not exist")
        return None


def write_file(file, statistics):
    """function for writing to file"""
    if statistics is None:
        return
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f"Lines: {statistics['lines']}, words:"
                f" {statistics['words']}, chars: {statistics['chars']} \n")


FILENAME = "test.txt"
final_result = read_file(FILENAME)
if final_result:
    print(f"lines = {final_result['lines']}, words = "
          f"{final_result['words']}, chars = {final_result['chars']}")
    write_file(FILENAME, final_result)
