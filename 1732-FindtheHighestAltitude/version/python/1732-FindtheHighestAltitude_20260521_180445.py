# Last updated: 5/21/2026, 6:04:45 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        left = [0] * len(nums)
4        right = [0] * len(nums)
5
6        left_sum =0
7        for i in range(len(nums)):
8            left_sum += nums[i]
9            left[i] = left_sum
10        
11        right_sum = 0
12        for j in range(len(nums)-1,-1,-1):
13            right_sum += nums[j]
14            right[j] = right_sum
15
16        total_sum = sum(nums)
17
18        for k in range(len(nums)):
19            strict_left = left[k] - nums[k]
20            strict_right = right[k] - nums[k]
21            if strict_left == strict_right:
22                return k
23            
24        return -1
25        