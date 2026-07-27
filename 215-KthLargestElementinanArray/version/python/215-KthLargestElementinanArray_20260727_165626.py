# Last updated: 7/27/2026, 4:56:26 PM
1import heapq
2
3class Solution:
4    def findKthLargest(self, nums: List[int], k: int) -> int:
5        min_heap = []
6
7        for num in nums:
8            heapq.heappush(min_heap,num)
9            if len(min_heap) > k:
10                heapq.heappop(min_heap)
11        
12        return min_heap[0]