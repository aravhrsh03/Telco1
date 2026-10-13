# 3. Rotate Array

n = int(input())
lis = list(map(int, input().split()))
k = int(input())

k %= n

temp = [0]*n

it = 0
for i in range(k):
    if i + k < n:
        temp[i + k] = lis[it]
        it += 1

for i in range(k):
    temp[i] = lis[it]
    it += 1
    
print(temp)