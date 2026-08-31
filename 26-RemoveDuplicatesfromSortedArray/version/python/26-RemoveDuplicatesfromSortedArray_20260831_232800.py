# Last updated: 8/31/2026, 11:28:00 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        left = 0
4
5        for right in range(len(nums)):
6            if nums[left] != nums[right]:
7                left += 1
8                nums[left] = nums[right]
9                   
10        return left+1
11