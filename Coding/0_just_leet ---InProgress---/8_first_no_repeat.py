# 8. First Non-Repeating Character

string = input()

freq = dict()
for ch in string:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

for ch in string:
    if freq.get(ch, 0) == 1:
        print(ch)
        break
else:
    print("Not found")