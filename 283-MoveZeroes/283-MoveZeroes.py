# Last updated: 5/13/2026, 4:43:10 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writer = 0
        
        # Pass 1: Overwrite the front of the array with non-zeros
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[writer] = nums[explorer]
                writer += 1
        
        # Pass 2: Fill the remaining positions with zeros
        for i in range(writer, len(nums)):
            nums[i] = 0