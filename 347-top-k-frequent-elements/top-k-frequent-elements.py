from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # считаем частоты
        # используем heap, чтобы получить k самых частых элементов
        return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]