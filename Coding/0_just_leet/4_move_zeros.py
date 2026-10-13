# 4. Move Zeros

n = int(input())
lis = list(map(int, input().split()))

i = 0
j = 0

while(j < n):
    if lis[j]:
        lis[i] = lis[j]
        i += 1
    j += 1

while(i < n):
    lis[i] = 0
    i += 1

print(lis)