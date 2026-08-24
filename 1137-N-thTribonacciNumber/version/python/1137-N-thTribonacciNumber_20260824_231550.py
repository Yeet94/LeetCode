# Last updated: 8/24/2026, 11:15:50 PM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        if n == 0:
4            return 0
5        if n == 1 or n == 2:
6            return 1
7
8        a,b,c = 0,1,1
9
10        for _ in range(3,n+1):
11            a,b,c = b,c,a+b+c
12        
13        return c