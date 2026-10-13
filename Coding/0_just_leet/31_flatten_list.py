def flatten_list(lis, res):
    for i in lis:
        if isinstance(i, list):
            flatten_list(i, res)
        else:
            res.append(i)
    return res

lis = [1, [2, [3, [4]], 5], 6]
print(flatten_list(lis,[]))