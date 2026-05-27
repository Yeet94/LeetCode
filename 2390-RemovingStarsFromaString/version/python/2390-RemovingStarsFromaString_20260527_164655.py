# Last updated: 5/27/2026, 4:46:55 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4        for char in s:
5            if char == "*":
6                stack.pop()
7            else:
8                stack.append(char)
9        
10        return "".join(stack)