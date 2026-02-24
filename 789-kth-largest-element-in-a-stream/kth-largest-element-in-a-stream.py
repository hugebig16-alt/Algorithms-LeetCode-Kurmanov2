import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Оставляем в куче только k самых больших элементов
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        # Если элементов меньше k, просто добавляем
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Если новый элемент больше минимального в куче
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        # Минимальный элемент — это k-й наибольший
        return self.heap[0]
