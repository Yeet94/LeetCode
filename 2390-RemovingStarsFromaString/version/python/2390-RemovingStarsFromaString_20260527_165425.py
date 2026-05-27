# Last updated: 5/27/2026, 4:54:25 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        s_list = list(s)
4        write = 0
5
6        for read in range(len(s_list)):
7            if s_list[read] == "*":
8                write -= 1
9            else:
10                s_list[write] = s_list[read]
11                write += 1
12            
13        return "".join(s_list[:write])