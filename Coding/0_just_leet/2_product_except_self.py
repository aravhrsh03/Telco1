# 2. Product Except Self (Hard)

n = int(input())
lis = list(map(int, input().split()))

pre = [lis[0]]
pos = [lis[n - 1]]

for i in range(1, n):
    pre.append(pre[i - 1] * lis[i])

j = 0
for i in range(n - 2, -1, -1):
    pos.append(pos[j] * lis[i])
    j += 1

pos = pos[::-1]

res = []
for i in range(n):
    left = 1
    right = 1
    if i + 1 < n:
        right = pos[i + 1]
    if i - 1 >= 0:
        left = pre[i - 1]
    res.append(right * left)

print(res)