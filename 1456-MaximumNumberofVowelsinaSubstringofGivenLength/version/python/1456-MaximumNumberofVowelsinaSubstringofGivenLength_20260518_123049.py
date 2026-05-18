# Last updated: 5/18/2026, 12:30:49 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = {"a","e","i","o","u"}
4        
5        initial_count = 0
6        for char in range(0,k):
7            if s[char] in vowels:
8                initial_count +=1
9         
10        max_num = initial_count
11
12        for i in range(k,len(s)):
13            if s[i] in vowels:
14                initial_count +=1
15            
16            if s[i-k] in vowels:
17                initial_count -=1
18        
19            max_num = max(initial_count,max_num)
20        
21        return max_num
22            