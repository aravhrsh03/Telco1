def my_filter(condition, iterable):
    iterators = iter(iterable)
    res = []

    while(True):
        try:
            value = next(iterators)
            if condition(value):
                res.append(value)
        except:
            break

    return res

print(my_filter(lambda x: x > 5, [1,6,3,8,2]))