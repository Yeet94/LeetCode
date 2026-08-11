# Last updated: 8/11/2026, 12:01:28 PM
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0

        start = []
        end = []
        left = 0
        right = len(costs) - 1

        while left < candidates:
            heapq.heappush(start,costs[left])
            left += 1
        
        while right >= len(costs) - candidates and right >= left:
            heapq.heappush(end,costs[right])
            right -= 1

        while k:
            if not end or (start and start[0] <= end[0]):
                val = heapq.heappop(start)
                total_cost += val
                
                if left <= right :
                    heapq.heappush(start,costs[left])
                    left += 1
            
            else:
                val = heapq.heappop(end)
                total_cost += val

                if left <= right:
                    heapq.heappush(end,costs[right])
                    right -= 1

            k-=1

        return total_cost
