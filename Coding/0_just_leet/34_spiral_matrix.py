def Spiral(mat):
    res_order = []

    top = 0
    right = len(mat[0]) - 1
    bottom = len(mat) - 1
    left = 0

    while (top <= bottom and left <= right):
        for i in range(left, right + 1):
            res_order.append(mat[top][i])

        top += 1
        for i in range(top, bottom + 1):
            res_order.append(mat[i][right])

        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res_order.append(mat[bottom][i])

        bottom -= 1
        if left <= right:
            for i in range(bottom, top -1, -1):
                res_order.append(mat[i][left])

        left += 1

    return res_order

matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15]
    ]

print(Spiral(matrix))