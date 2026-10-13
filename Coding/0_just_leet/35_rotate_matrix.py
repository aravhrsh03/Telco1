def printMatrix(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()

def rotate(mat):
    res_matrix = []

    ROW = len(matrix) -1
    COL = len(matrix[0])

    for j in range(COL):
        current_row = []
        for i in range(ROW, -1, -1):
            current_row.append(mat[i][j])
        res_matrix.append(current_row)

    return res_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

printMatrix(rotate(matrix))