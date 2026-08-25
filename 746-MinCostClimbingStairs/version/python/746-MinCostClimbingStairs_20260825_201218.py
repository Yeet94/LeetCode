# Last updated: 8/25/2026, 8:12:18 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        first = cost[0]
4        second = cost[1]
5
6        for i in range(2,len(cost)):
7            curr = cost[i] + min(first,second)
8            first,second = second,curr
9        
10        return min(first,second)
11
12
13            