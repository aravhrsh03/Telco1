def compare(record1, record2):
    salary1 = record1[1]
    salary2 = record2[1]

    if salary1 < salary2:
        return -1
    elif salary1 > salary2:
        return 1
    else:
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