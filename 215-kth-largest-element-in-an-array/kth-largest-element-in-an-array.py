import heapq
import random

class Solution:
    # Вариант с min-heap
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]
    
    # Вариант с quickselect (без сортировки)
    # def findKthLargest(self, nums, k):
    #     k = len(nums) - k
    #     def quickselect(left, right):
    #         pivot_index = random.randint(left, right)
    #         pivot = nums[pivot_index]
    #         nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    #         store_index = left
    #         for i in range(left, right):
    #             if nums[i] < pivot:
    #                 nums[i], nums[store_index] = nums[store_index], nums[i]
    #                 store_index += 1
    #         nums[store_index], nums[right] = nums[right], nums[store_index]
    #         if store_index == k:
    #             return nums[store_index]
    #         elif store_index < k:
    #             return quickselect(store_index + 1, right)
    #         else:
    #             return quickselect(left, store_index - 1)
    #     return quickselect(0, len(nums) - 1)