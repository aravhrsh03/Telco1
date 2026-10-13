def cache(func):
    cache_dict = {}

    def wrapper(*args):
        key = args

        if key in cache_dict:
            print("Cache Return", end=" ")
            return cache_dict[key]

        value = func(*args)
        cache_dict[key] = value
        return value

    return wrapper


@cache
def square(n):
    return n * n


print(square(5))
print(square(5))