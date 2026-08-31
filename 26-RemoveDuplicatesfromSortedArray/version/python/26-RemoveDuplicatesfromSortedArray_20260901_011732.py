# Last updated: 9/1/2026, 1:17:32 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if len(nums) <= 2:
4            return len(nums)
5        k = 2
6        for i in range(2,len(nums)):
7            if nums[i] != nums[k-2]:
8                nums[k] = nums[i]
9                k += 1
10        
11        return k
12