# Last updated: 5/11/2026, 11:40:02 AM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        writer = 0
7
8        for explorer in range(len(nums)):
9            if nums[explorer] != 0:
10                if writer < explorer:
11                    nums[writer], nums[explorer] = nums[explorer], nums[writer]
12
13                writer +=1