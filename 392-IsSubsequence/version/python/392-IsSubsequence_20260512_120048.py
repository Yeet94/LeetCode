# Last updated: 5/12/2026, 12:00:48 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        if not s:
4            return True
5        
6        ps = 0
7        for char in t:
8            if s[ps] == char:
9                ps +=1
10
11            if ps == len(s):
12                return True
13                
14        return False