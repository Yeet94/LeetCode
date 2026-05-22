# Last updated: 5/22/2026, 5:39:01 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        set1 = set(nums1)
4        set2 = set(nums2)
5
6        return [list(set1-set2),list(set2-set1)]
7