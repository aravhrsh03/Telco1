# 1. Two Sum (Medium)

n = int(input())
lis = list(map(int, input().split()))
target = int(input())

index = {}
for i in range(n):
    index[lis[i]] = i

dic = {}
for i in lis:
    remain = target - i
    getVal = dic.get(remain, 0)
    if getVal == i:
        print([index[remain], index[dic[remain]]])
        break
    dic[i] = target - i