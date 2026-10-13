def Transpose(mat):
    result_matrix = []

    ROW = len(mat)
    COL = len(mat[0])

    for j in range(COL):
        current_row = []
        for i in range(ROW):
            current_row.append(mat[i][j])
        result_matrix.append(current_row)

    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(Transpose(matrix))