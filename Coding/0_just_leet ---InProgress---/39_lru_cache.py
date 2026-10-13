from enum import Enum

class Actions(Enum):
    PUT = "PUT"
    GET = "GET"

class CONFIG:
    frames = 4

def PUT_Works(frames, key, cache, value):
    if cache.get(key) != None:
        position = 0
        for i in range(len(frames)):
            if frames[i] == key:
                position = i
                break

        while position + 1 < len(frames):
            frames[position] = frames[position + 1]
            position += 1

        frames[position] = key

    elif len(frames) >= CONFIG.frames:
        removed = frames.pop(0)
        del cache[removed]
        cache[key] = value
        frames.append(key)
    else:
        cache[key] = value
        frames.append(key)

def GET_Works(cache, key, frames):
    if cache.get(key) != None:
        position = 0
        for i in range(len(frames)):
            if frames[i] == key:
                position = i
                break

        while position + 1 < len(frames):
            frames[position] = frames[position + 1]
            position += 1

        frames[position] = key
    return cache.get(key, -1)

def do_action(action, key, value, cache, frames):
    match action:
        case Actions.PUT.value:
            PUT_Works(frames, key, cache, value)

        case Actions.GET.value:
            print(GET_Works(cache, key, frames))

def lru(pages):
    frames = []
    cache = dict()
    for i in pages:
        action = i[0]
        key = i[1]
        value = None
        if len(i) > 2:
            value = i[2]
        do_action(action, key, value, cache, frames)
    return frames

test_case = [
    ("PUT", "A", 1),
    ("PUT", "B", 2),
    ("PUT", "C", 3),
    ("GET", "A"),
    ("PUT", "D", 4),
    ("GET", "B"),
    ("PUT", "E", 5),

    ("PUT", "D", 4),
    ("PUT", "F", 6),
    ("GET", "A")
]
print(lru(pages=test_case))