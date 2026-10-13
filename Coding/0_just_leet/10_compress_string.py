# 10. Compress String

string = input()

result = ""

cur = string[0]
cnt = 0

for ch in string:
    if ch == cur:
        cnt += 1
    else:
        result += cur
        result += str(cnt)
        cur = ch
        cnt = 1
if cnt:
    result += cur
    result += str(cnt)

print(result)