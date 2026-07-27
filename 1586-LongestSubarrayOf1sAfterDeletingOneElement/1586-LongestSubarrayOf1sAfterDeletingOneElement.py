# Last updated: 7/27/2026, 4:13:42 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        count = 0 
        max_num = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count +=1
            
            while count >1:
                if nums[left] == 0:
                    count -=1
                left +=1
            
            max_num = max(max_num, right - left)
        
        return max_num