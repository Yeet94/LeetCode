# Last updated: 7/27/2026, 4:14:08 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_window_sum = sum(nums[0:k])
        max_sum = current_window_sum
        
        for i in range(1, len(nums) - k + 1):
            current_window_sum = current_window_sum - nums[i-1] + nums[i+k-1] 
            max_sum = max(current_window_sum, max_sum)

        return max_sum / k
                
            


