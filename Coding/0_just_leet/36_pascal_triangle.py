def printMatrix(mat):
    width = 4
    total_width = len(mat[-1]) * width

    for row in mat:
        current = ""

        for num in row:
            current += f"{num:{width}}"

        spaces = (total_width - len(current)) // 2

        print(" " * spaces + current)

def create_pascal(n):
    res = [[1], [1, 1]]

    i = 2
    while i < n:
        load_last = res[-1]
        current_row = [1]

        for i in range(1, len(load_last)):
            current_row.append(load_last[i] + load_last[i - 1])

        current_row.append(1)

        res.append(current_row)

    return res

printMatrix(create_pascal(10))
