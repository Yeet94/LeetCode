# Last updated: 5/14/2026, 11:09:13 AM
1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3       # 1. Manually define the sorting logic
4        def merge_sort(arr):
5            if len(arr) <= 1:
6                return arr
7            
8            mid = len(arr) // 2
9            left = merge_sort(arr[:mid])
10            right = merge_sort(arr[mid:])
11            
12            return merge(left, right)
13
14        def merge(left, right):
15            result = []
16            i = j = 0
17            while i < len(left) and j < len(right):
18                if left[i] < right[j]:
19                    result.append(left[i])
20                    i += 1
21                else:
22                    result.append(right[j])
23                    j += 1
24            result.extend(left[i:])
25            result.extend(right[j:])
26            return result
27
28        # 2. Call your sort
29        nums = merge_sort(nums)
30
31        # 3. Your Two-Pointer logic (using small steps, not jumps!)
32        l, r = 0, len(nums) - 1
33        count = 0
34        while l < r:
35            total = nums[l] + nums[r]
36            if total == k:
37                count += 1
38                l += 1
39                r -= 1
40            elif total < k:
41                l += 1
42            else:
43                r -= 1
44                
45        return count