# 6. Group Anagrams

n = int(input())
lis = list(map(str, input().split()))

ana = dict()

for i in lis:
    sor = "".join(sorted(i))
    
    if sor in ana:
        ana[sor].append(i)
    else:
        ana[sor] = [i]

print(ana)