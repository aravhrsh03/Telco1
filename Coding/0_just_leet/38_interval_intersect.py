def get_intersection(A, B):
    res = []

    for i in range(len(A)):
        a = A[i]
        b = B[i]

        start = max(a[0], b[0])
        end = min(a[1], b[1])

        if start <= end:
            res.append([start, end])

    return res

A = [[1, 5], [10, 14]]
B = [[2, 6], [8, 10]]

print(get_intersection(A, B))