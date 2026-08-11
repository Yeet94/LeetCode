# Last updated: 8/11/2026, 12:01:26 PM
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1,nums2, range(len(nums1))), key=lambda x : x[1], reverse = True)

        min_heap = []
        min_idx = set()

        running_sum = 0
        max_score = 0 

        for num1, num2, i in pairs:
            heapq.heappush(min_heap,(num1,i))
            min_idx.add(i)
            running_sum += num1

            if len(min_heap) > k:
                popped_val, popped_id = heapq.heappop(min_heap)
                min_idx.remove(popped_id)
                running_sum -= popped_val

            if len(min_heap) == k:
                max_score = max(max_score, running_sum*num2)


        return max_score                


