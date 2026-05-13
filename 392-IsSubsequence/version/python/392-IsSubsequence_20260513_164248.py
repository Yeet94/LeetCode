# Last updated: 5/13/2026, 4:42:48 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        
4        L = 0
5        R = len(height) -1
6
7        max_area = 0
8
9        while L < R:
10            h_left = height[L]
11            h_right = height[R]
12
13            current_h = min(h_left,h_right)
14            max_area = max(max_area, current_h * (R-L))
15
16            if h_left < h_right:
17                while L<R and height[L] <= h_left:
18                    L +=1
19            else:
20                while L<R and height[R] <= h_right:
21                    R -=1
22            
23        return max_area