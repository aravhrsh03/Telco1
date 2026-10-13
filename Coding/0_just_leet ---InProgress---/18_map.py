def my_map(function, iterable):
    iterator = iter(iterable)
    res = []
    while(True):
        try:
            value = next(iterator)
            res.append(function(value))
        except:
            break

    return res

def double(x):
    return x * 2

print(my_map(double, [1, 2, 3, 4, 5]))