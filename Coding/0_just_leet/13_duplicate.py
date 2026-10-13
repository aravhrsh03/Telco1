def get_duplicates(files):
    file = set()
    dup = []
    for k, v in files.items():
        for i in v:
            if i in file:
                dup.append(i)
            else:
                file.add(i)
    return dup

files = {
    "A": ["a.txt", "b.txt"],
    "B": ["x.txt", "y.txt"],
    "C": ["b.txt", "z.txt"]
}

print(get_duplicates(files))