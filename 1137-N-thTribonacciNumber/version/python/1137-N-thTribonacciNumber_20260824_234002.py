# Last updated: 8/24/2026, 11:40:02 PM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        memo = {}
4
5        def helper(k:int) -> int:
6            if k == 0:
7                return 0
8            if k == 1 or k == 2:
9                return 1
10            if k in memo:
11                return memo[k]
12            
13            memo[k] = helper(k-1) + helper(k-2) + helper(k-3)
14            return memo[k]
15
16        return helper(n)