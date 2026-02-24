import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Используем max-heap через отрицательные значения
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Берем два самых тяжелых камня
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            # Если веса разные, добавляем разницу обратно
            if first != second:
                heapq.heappush(heap, -(first - second))

        # Если камень остался, возвращаем его вес
        return -heap[0] if heap else 0
