# Last updated: 8/24/2026, 11:42:21 PM
1from functools import lru_cache
2
3class Solution:
4    @lru_cache(maxsize=None)
5    def tribonacci(self, n: int) -> int:
6        if n == 0:
7            return 0
8        if n == 1 or n == 2:
9            return 1
10        
11        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)