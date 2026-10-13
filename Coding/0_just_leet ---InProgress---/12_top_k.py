import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)

    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))