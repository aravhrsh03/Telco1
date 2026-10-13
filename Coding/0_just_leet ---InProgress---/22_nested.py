def compare(record1, record2):
    name1, age1, salary1 = record1
    name2, age2, salary2 = record2

    if age1 < age2:
        return -1
    elif age1 > age2:
        return 1

    if salary1 > salary2:
        return -1
    elif salary1 < salary2:
        return 1

    if name1 < name2:
        return -1
    elif name1 > name2:
        return 1

    return 0

def my_sort(employees, compare):
    n = len(employees)

    for i in range(n):
        for j in range(0, n - i - 1):

            if compare(employees[j], employees[j + 1]) > 0:
                employees[j], employees[j + 1] = employees[j + 1], employees[j]

    return employees

employees = [
    ("John", 50000),
    ("Alex", 90000),
    ("David", 70000)
]

print(my_sort(employees, compare))