# Last updated: 8/26/2026, 12:00:52 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        first,second = 0,0
4
5        for num in nums:
6            curr = max(second,first+num)
7            first,second = second,curr
8
9        return second