# Last updated: 6/24/2026, 10:39:59 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        pair_id = {}
4
5        for i,num in enumerate(nums):
6            if target-num in pair_id:
7                return [i,pair_id[target-num]]
8            pair_id[num] = i