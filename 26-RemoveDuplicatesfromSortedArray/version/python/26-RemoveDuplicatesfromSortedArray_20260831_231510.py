# Last updated: 8/31/2026, 11:15:10 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 0
4        dup = set()
5
6        for i,char in enumerate(nums):
7            if char not in dup:
8                nums[k] = char
9                dup.add(char)
10                k += 1
11
12        return k