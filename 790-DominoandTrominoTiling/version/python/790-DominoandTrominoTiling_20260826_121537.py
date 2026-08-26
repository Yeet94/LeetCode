# Last updated: 8/26/2026, 12:15:37 PM
1class Solution:
2    def numTilings(self, n: int) -> int:
3        MOD = int(1e9 + 7)
4        if n == 1:
5            return 1
6        if n == 2:
7            return 2
8        
9        # Base states
10        f_prev2 = 1  # f(0)
11        f_prev1 = 1  # f(1)
12        f_curr  = 2  # f(2)
13        p_curr  = 1  # p(2)
14
15        for i in range(3,n+1):
16            f_next = (f_curr + f_prev1 + 2*(p_curr)) % MOD
17            p_next = (p_curr + f_prev1) % MOD
18
19            f_prev2, f_prev1, f_curr = f_prev1, f_curr, f_next
20            p_curr = p_next
21            
22        return f_curr
23