# Last updated: 7/27/2026, 4:13:50 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1-set2),list(set2-set1)]
