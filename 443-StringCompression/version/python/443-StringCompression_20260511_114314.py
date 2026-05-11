# Last updated: 5/11/2026, 11:43:14 AM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        writer = 0
4        
5        # Pass 1: Overwrite the front of the array with non-zeros
6        for explorer in range(len(nums)):
7            if nums[explorer] != 0:
8                nums[writer] = nums[explorer]
9                writer += 1
10        
11        # Pass 2: Fill the remaining positions with zeros
12        for i in range(writer, len(nums)):
13            nums[i] = 0