import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # превращаем все камни в отрицательные числа для max-heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            # достаем два самых тяжелых камня
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            if first != second:
                # если камни не равны, разница возвращается в кучу
                heapq.heappush(heap, -(first - second))
        
        return -heap[0] if heap else 0