"""Homework 14: files"""


def write_data(file):
    """Write data to file"""
    students = [
        ("Аndrey Sirota", "Group №1", [6, 8, 10, 5, 3]),
        ("Evgeniy Kondratiev", "Group №2", [5, 7, 2, 5]),
        ("Raman Minin", "Group №1", [5, 7]),
        ("Maria Sharko", "Group №2", [3, 4, 8]),
    ]
    try:
        with open(file, "w", encoding='utf-8') as f:
            for name, group, grades in students:
                f.write(f"{name}, {group},{','.join(map(str, grades))}\n")
    except PermissionError:
        print(f"Error: No permission to write to file '{file}'.")


def read_data(file):
    """Read data from file"""
    total = 0
    count: dict[str, int] = {}
    sum_grades: dict[str, float] = {}
    n_grades: dict[str, int] = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) < 3:
                continue
            group = parts[1]
            grades = []
            valid = True
            for part in parts[2:]:
                try:
                    grade = int(part)
                    grades.append(grade)
                except ValueError:
                    valid = False
                    break
            if not valid:
                continue
            total += 1
            if group in count:
                count[group] += 1
            else:
                count[group] = 1
            if group in sum_grades:
                sum_grades[group] += sum(grades)
            else:
                sum_grades[group] = sum(grades)
            if group in n_grades:
                n_grades[group] += len(grades)
            else:
                n_grades[group] = len(grades)
    return total, count, sum_grades, n_grades


def append_data(file, total, count, sum_grades, n_grades):
    """Append data to file"""
    try:
        with open(file, "a", encoding='utf-8') as f:
            f.write(f"Total number of students: {total}\n")
            for g in sorted(count):
                average = sum_grades[g] / n_grades[g] if n_grades[g] else 0.0
                f.write(f"{g}: number of students = {count[g]},"
                        f" average score = {average:.2f}\n")
    except FileNotFoundError:
        print(f"Error: file '{file}' not found.")
    except PermissionError:
        print(f"Error: Insufficient permissions to operate the file '{file}'.")


def main():
    """Function main"""
    file = "students.txt"
    write_data(file)
    total, count, sum_grades, n_grades = read_data(file)
    print(f"Total number of students: {total}")
    for g in sorted(count):
        avg = sum_grades[g] / n_grades[g] if n_grades[g] else 0.0
        print(f"{g}: students = {count[g]}, average score = {avg:.2f}")
    append_data(file, total, count, sum_grades, n_grades)


if __name__ == "__main__":
    main()
