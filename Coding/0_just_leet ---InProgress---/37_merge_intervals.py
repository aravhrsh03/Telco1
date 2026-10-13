def check(first, second):
    return first[1] >= second[0]

def merge_interval(lis):
    lis.sort()
    print(lis)
    res = []
    current = lis[0]

    for i in range(1, len(lis)):
        track = lis[i]

        if check(current, track):
            current = [current[0], max(current[1], track[1])]
        else:
            res.append(current)
            current = track

    res.append(current)

    return res


lis = [
    [1, 10],
    [2, 6],
    [3, 5],
    [7, 12],
    [11, 15],
    [14, 20],
    [21, 25]
]

print(merge_interval(lis=lis))