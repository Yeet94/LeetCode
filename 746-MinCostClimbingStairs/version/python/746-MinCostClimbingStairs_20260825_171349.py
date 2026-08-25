# Last updated: 8/25/2026, 5:13:49 PM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        
4        if n == 0:
5            return 0
6        if n == 1 or n == 2:
7            return 1
8
9        a,b,c = 0,1,1
10
11        for _ in range(3,n+1):
12            a,b,c = b,c,a+b+c
13
14        return c
15
16
17            
18        
19        