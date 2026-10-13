# 5. Longest Consecutive Sequence

n = int(input())
lis = list(map(int, input().split()))

set_lis = set(lis)
longest = 0

for i in set_lis:
    if i - 1 not in set_lis:
        length = 1
        while i + length in set_lis:
            length += 1
        longest = max(longest, length)

print(longest) 