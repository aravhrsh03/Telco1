def get_fib():
    first = 0
    second = 1

    yield first
    yield second

    while(True):
        yield first + second

        third = first + second
        first = second
        second = third

fib = get_fib()
for i in range(8):
    print(next(fib))
else:
    print("...")