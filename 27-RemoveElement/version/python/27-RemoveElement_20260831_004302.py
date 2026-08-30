# Last updated: 8/31/2026, 12:43:02 AM
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        curr = 0
4        k = 0
5
6        while curr < len(nums):
7            # Guard against running past the end of the array
8            while curr < len(nums) and nums[curr] == val:
9                curr += 1
10            
11            # If curr reached the end after skipping, stop
12            if curr == len(nums):
13                break
14
15            # Assign (= instead of ==)
16            nums[k] = nums[curr]
17            k += 1
18            curr += 1
19
20        # Return the count (an integer), not a list slice
21        return k