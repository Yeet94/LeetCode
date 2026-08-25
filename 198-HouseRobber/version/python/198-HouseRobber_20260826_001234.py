# Last updated: 8/26/2026, 12:12:34 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        memo = {}
4        n = len(nums)
5
6        def helper(k:int) -> int:
7            if k < 0:
8                return 0
9            if k == 0:
10                return nums[0]
11
12            if k in memo:
13                return memo[k]
14
15            memo[k] = max(helper(k-2)+nums[k], helper(k-1))
16
17            return memo[k]
18
19        return helper(n-1)