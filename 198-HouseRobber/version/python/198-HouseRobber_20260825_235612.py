# Last updated: 8/25/2026, 11:56:12 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        #if only have one house
4        if len(nums) == 1:
5            return nums[0]
6
7        first = nums[0]
8        second = max(nums[0],nums[1])
9
10        for i in range(2,len(nums)):
11            curr = max(first+nums[i],second)
12            first,second = second,curr
13        
14        return second
15        