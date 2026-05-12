# Last updated: 5/12/2026, 5:31:54 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        dic = {}
4
5        #Preprocess t
6        for i,char in enumerate(t):
7            if char not in dic:
8                dic[char] = []
9            dic[char].append(i)
10        
11        current_pos = -1
12        for char in s:
13            if char not in dic:
14                return False
15            
16            next_idx = -1
17            indicies = dic[char]
18
19            l,r = 0, len(indicies)-1
20
21            while l <= r:
22                mid = (l+r)//2
23                if indicies[mid] > current_pos:
24                    next_idx = indicies[mid]
25                    r = mid - 1
26                
27                else:
28                    l = mid + 1
29            
30            if next_idx == -1:
31                return False
32            
33            current_pos = next_idx
34        
35        return True
36        
37