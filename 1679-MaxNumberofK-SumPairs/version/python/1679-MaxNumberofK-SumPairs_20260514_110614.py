# Last updated: 5/14/2026, 11:06:14 AM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        if not nums:
4            return 0
5
6        nums.sort()
7
8        l,r = 0, len(nums) - 1
9        count = 0
10        while l<r:
11            total = nums[l] + nums[r]
12            if total < k:
13                l += 1
14            elif total > k:
15                r -= 1
16            else:
17                count +=1
18                l +=1
19                r -=1
20                
21        
22        return count