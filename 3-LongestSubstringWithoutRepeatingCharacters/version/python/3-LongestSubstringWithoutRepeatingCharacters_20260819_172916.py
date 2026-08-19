# Last updated: 8/19/2026, 5:29:16 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = {}
4        left = 0 
5        max_len = 0
6
7        for right,char in enumerate(s):
8            if char in seen and seen[char] >= left:
9                left = seen[char] + 1
10
11            seen[char] = right
12
13            max_len = max(max_len, right - left + 1) 
14
15        return max_len