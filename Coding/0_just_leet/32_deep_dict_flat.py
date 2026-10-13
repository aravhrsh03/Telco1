def deep_dict_flat(dictionary, res, track_key):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            track_key.append(str(key))
            deep_dict_flat(value, res, track_key)
        if not isinstance(value, dict):
            track_key.append(str(key))
            res[".".join(track_key)] = value
            track_key.clear()
    return res

dictionary = {
    "a": {
        "b": {
            "c": 10
        }
    },
    "d": {
        "z": 20
    }
}

print(deep_dict_flat(dictionary, dict(), []))