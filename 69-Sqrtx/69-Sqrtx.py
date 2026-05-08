# Last updated: 5/8/2026, 4:23:23 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        #sqrt of x is always less than or equal to x//2, hence narrow search
        left = 2
        right = x//2

        while left <= right:
            pivot = (right+left)//2
            num = pivot*pivot

            if num == x:
                return pivot
            elif num < x:
                left = pivot+1
            else:
                right = pivot-1

        return left-1
                