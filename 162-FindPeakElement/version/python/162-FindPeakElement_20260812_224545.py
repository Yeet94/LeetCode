# Last updated: 8/12/2026, 10:45:45 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        start = 0
4        end = len(nums) - 1
5
6        while start < end:
7            mid = start + (end - start)//2
8
9            if nums[mid] < nums[mid+1]:
10                start = mid + 1
11            
12            else:
13                end = mid
14
15        return start