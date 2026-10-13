# 7. Longest Substring Without Repeating Characters

lis = input()

n = len(lis)

left = 0
right = 0

longest = 0

seen = set()

while left < n and right < n:
    if lis[right] not in seen:
        seen.add(lis[right])
        right += 1
        longest = max(longest, right - left)
    else:
        seen.remove(lis[left])
        left += 1

print(longest)