def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line

file_name = "./data.txt"
gen = read_file(file_name)

while True:
    try:
        line = next(gen)
        print(line, end="")
    except StopIteration:
        print("\nEnd Of File")
        break