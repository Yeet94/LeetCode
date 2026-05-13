# Last updated: 5/13/2026, 4:43:25 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        L = 0
        R = len(height) -1

        max_area = 0

        while L < R:
            h_left = height[L]
            h_right = height[R]

            current_h = min(h_left,h_right)
            max_area = max(max_area, current_h * (R-L))

            if h_left < h_right:
                while L<R and height[L] <= h_left:
                    L +=1
            else:
                while L<R and height[R] <= h_right:
                    R -=1
            
        return max_area