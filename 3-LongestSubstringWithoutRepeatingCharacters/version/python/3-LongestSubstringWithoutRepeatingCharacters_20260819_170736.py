# Last updated: 8/19/2026, 5:07:36 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        
4        char = set()
5        left = 0
6        max_length = 0
7
8        for right in range(len(s)):
9            
10            while s[right] in char:
11                char.remove(s[left])
12                left +=1
13            
14            char.add(s[right])
15            max_length = max(max_length, len(char))
16
17        return max_length
18        