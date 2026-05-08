# Last updated: 5/8/2026, 4:22:49 PM
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums
        
        suffix_max = [0] * n
        current_max = -1

        for i in range(n-1,-1,-1):
            suffix_max[i] = current_max
            current_max = max(suffix_max[i], nums[i])
        
        left_max = -1
        res = []

        for i in range(n):
            if i ==0 or i ==n-1:
                res.append(nums[i])
            elif nums[i] > left_max or nums[i] > suffix_max[i]:
                res.append(nums[i])
            
            left_max = max(left_max,nums[i])
        
        return res
        