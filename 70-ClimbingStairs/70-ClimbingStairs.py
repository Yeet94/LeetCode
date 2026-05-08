# Last updated: 5/8/2026, 4:23:22 PM
from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)