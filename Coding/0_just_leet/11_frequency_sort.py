from collections import defaultdict

lis = list(map(int, input().split()))

freq = defaultdict(int)

for x in lis:
    freq[x] += 1

items = sorted(freq.items(), key=lambda x: -x[1])

res = []

for num, count in items:
    res.extend([num] * count)

print(res)