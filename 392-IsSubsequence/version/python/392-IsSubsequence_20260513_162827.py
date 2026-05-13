# Last updated: 5/13/2026, 4:28:27 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        L = 0
4        R = len(height) - 1
5
6        max_area = 0
7        while L < R:
8            area = min(height[L], height[R]) * (R-L)
9            max_area = max(max_area, area)
10            if height[L] < height[R]:
11                L += 1
12            else:
13                R -= 1  
14            
15        return max_area