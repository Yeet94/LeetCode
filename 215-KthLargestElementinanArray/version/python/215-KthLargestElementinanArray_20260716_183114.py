# Last updated: 7/16/2026, 6:31:14 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        pivot = nums[len(nums)//2]
4
5        left = []
6        middle = []
7        right = []
8
9        for x in nums:
10            if x < pivot:
11                left.append(x)
12            elif x==pivot:
13                middle.append(x)
14            else:
15                right.append(x)
16    
17        # Case 1: The target is in the larger elements pool
18        if k <= len(right):
19            return self.findKthLargest(right, k)
20            
21        # Case 2: The target is one of our pivot elements
22        elif k <= len(right) + len(middle):
23            return pivot
24            
25        # Case 3: The target is in the smaller elements pool
26        else:
27            # We discard right and middle, so we subtract their sizes from k
28            new_k = k - len(right) - len(middle)
29            return self.findKthLargest(left, new_k)
30