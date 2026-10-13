def merge(d1, d2):
    result = d1.copy()

    for key in d2:
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(d2[key], dict)
        ):
            result[key] = merge(result[key], d2[key])
        else:
            result[key] = d2[key]

    return result


d1 = {
    "a": {
        "x": 1
    }
}

d2 = {
    "a": {
        "y": 2
    }
}

print(merge(d1, d2))