def my_reduce(function, iterable):
    iterator = iter(iterable)

    res = next(iterator)

    while True:
        try:
            value = next(iterator)
            res = function(res, value)

        except StopIteration:
            break

    return res

def maximum(a, b):
    if a > b:
        return a
    return b


print(my_reduce(maximum, [4, 9, 2, 7]))