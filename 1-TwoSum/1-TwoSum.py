# Last updated: 5/8/2026, 4:24:03 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i,nums in enumerate(nums):
            if target - nums in pair_idx:
                return [i,pair_idx[target-nums]]
            pair_idx[nums] = i