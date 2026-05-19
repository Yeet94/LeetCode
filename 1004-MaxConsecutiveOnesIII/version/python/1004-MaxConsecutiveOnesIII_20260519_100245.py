# Last updated: 5/19/2026, 10:02:45 AM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left = 0
4        zero_count = 0
5        max_count = 0
6
7        for right in range(len(nums)):
8
9            if nums[right] == 0:
10                zero_count += 1
11            
12            while zero_count > k:
13                if nums[left] == 0:
14                    zero_count -=1
15                left +=1
16            
17            max_count = max(max_count, right - left + 1)
18        
19        return max_count
20
21            
22            
23            