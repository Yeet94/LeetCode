# Last updated: 5/20/2026, 10:53:20 AM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        
4        left = 0
5        count = 0 
6        max_num = 0
7
8        for right in range(len(nums)):
9            if nums[right] == 0:
10                count +=1
11            
12            while count >1:
13                if nums[left] == 0:
14                    count -=1
15                left +=1
16            
17            max_num = max(max_num, right - left)
18        
19        return max_num