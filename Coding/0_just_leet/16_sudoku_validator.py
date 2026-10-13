def validate(row):
    if len(row) != 9:
        return False
    if min(row) < 1 or max(row) > 9:
        return False
    return len(set(row)) == 9

row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row2 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
row3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(validate(row1))  
print(validate(row2))  
print(validate(row3))  