# Last updated: 5/27/2026, 4:45:12 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4        right = 0
5        while right < len(s):
6            if s[right] == "*":
7                stack.pop()
8            else:
9                stack.append(s[right])
10
11            right += 1
12        
13        return "".join(stack)
14            