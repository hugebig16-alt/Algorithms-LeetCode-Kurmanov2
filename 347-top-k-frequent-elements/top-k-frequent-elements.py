from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Считаем, сколько раз встречается каждый элемент
        count = Counter(nums)

        # Берем k элементов с наибольшей частотой
        return [item for item, freq in heapq.nlargest(
            k, count.items(), key=lambda x: x[1]
        )]
