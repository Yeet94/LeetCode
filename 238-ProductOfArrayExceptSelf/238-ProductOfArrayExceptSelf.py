# Last updated: 5/8/2026, 4:22:56 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # We initialize the result array with 1s. 
        # This is the ONLY array we will use.
        res = [1] * n
        
        # Pass 1: Build the Prefix (Left side)
        # res[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate Suffix on the fly and multiply
        # We walk backward and maintain a 'suffix' variable
        suffix = 1
        for i in range(n - 1, -1, -1):
            # Current res[i] (the left product) * current suffix (the right product)
            res[i] *= suffix
            # Update the suffix to include nums[i] for the next element to the left
            suffix *= nums[i]
            
        return res