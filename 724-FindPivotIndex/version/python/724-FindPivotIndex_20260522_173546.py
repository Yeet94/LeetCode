# Last updated: 5/22/2026, 5:35:46 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        set1 = set()
4        set2 = set()
5
6        for char in nums1:
7            set1.add(char)
8        
9        for char in nums2:
10            set2.add(char)
11
12        arr1 = []
13        arr2 = []
14
15        for char1 in set1:
16            if char1 not in set2:
17                arr1.append(char1)
18        
19        for char2 in set2:
20            if char2 not in set1:
21                arr2.append(char2)
22
23        answer = [arr1,arr2]
24        return answer