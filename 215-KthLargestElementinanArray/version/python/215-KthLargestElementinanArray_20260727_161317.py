# Last updated: 7/27/2026, 4:13:17 PM
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
12            elif x > pivot:
13                right.append(x)
14            else:
15                middle.append(x)
16
17
18        if k <= len(right):
19            return self.findKthLargest(right,k)
20        
21        elif k <= len(middle) + len(right):
22            return pivot
23
24        else:
25            new_k = k - len(middle) - len(right)
26            return self.findKthLargest(left,new_k)