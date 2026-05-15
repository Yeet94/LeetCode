# Last updated: 5/15/2026, 12:02:41 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        current_window_sum = sum(nums[0:k])
4        max_sum = current_window_sum
5        
6        for i in range(1, len(nums) - k + 1):
7            current_window_sum = current_window_sum - nums[i-1] + nums[i+k-1] 
8            max_sum = max(current_window_sum, max_sum)
9
10        return max_sum / k
11                
12            
13
14
15