# Last updated: 8/3/2026, 5:48:16 PM
1import heapq
2class Solution:
3    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
4        total_cost = 0
5
6        start = []
7        end = []
8        left = 0
9        right = len(costs) - 1
10
11        while left < candidates:
12            heapq.heappush(start,costs[left])
13            left += 1
14        
15        while right >= len(costs) - candidates and right >= left:
16            heapq.heappush(end,costs[right])
17            right -= 1
18
19        while k:
20            if not end or (start and start[0] <= end[0]):
21                val = heapq.heappop(start)
22                total_cost += val
23                
24                if left <= right :
25                    heapq.heappush(start,costs[left])
26                    left += 1
27            
28            else:
29                val = heapq.heappop(end)
30                total_cost += val
31
32                if left <= right:
33                    heapq.heappush(end,costs[right])
34                    right -= 1
35
36            k-=1
37
38        return total_cost
39