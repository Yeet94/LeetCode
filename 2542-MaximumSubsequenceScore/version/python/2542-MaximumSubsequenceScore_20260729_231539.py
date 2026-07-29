# Last updated: 7/29/2026, 11:15:39 PM
1import heapq
2
3class Solution:
4    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
5        pairs = sorted(zip(nums1,nums2, range(len(nums1))), key=lambda x : x[1], reverse = True)
6
7        min_heap = []
8        min_idx = set()
9
10        running_sum = 0
11        max_score = 0 
12
13        for num1, num2, i in pairs:
14            heapq.heappush(min_heap,(num1,i))
15            min_idx.add(i)
16            running_sum += num1
17
18            if len(min_heap) > k:
19                popped_val, popped_id = heapq.heappop(min_heap)
20                min_idx.remove(popped_id)
21                running_sum -= popped_val
22
23            if len(min_heap) == k:
24                max_score = max(max_score, running_sum*num2)
25
26
27        return max_score                
28
29
30