import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Берем первые k элементов и делаем из них min-heap
        heap = nums[:k]
        heapq.heapify(heap)

        # Проходим по остальным элементам
        for num in nums[k:]:
            # Если элемент больше минимального в куче
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # Минимальный элемент в куче — это k-й наибольший
        return heap[0]
