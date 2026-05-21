# Last updated: 5/21/2026, 6:16:05 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total_sum = sum(nums)
4        left_sum = 0
5
6        for i in range(len(nums)):
7            right_sum = total_sum - left_sum - nums[i]
8            if left_sum == right_sum:
9                return i
10
11            left_sum += nums[i]
12            
13        return -1