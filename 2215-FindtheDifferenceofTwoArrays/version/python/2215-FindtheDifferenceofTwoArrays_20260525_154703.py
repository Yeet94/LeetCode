# Last updated: 5/25/2026, 3:47:03 PM
1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3        
4        if len(word1) != len(word2):
5            return False
6        
7        dic1 = {}
8        dic2 = {}
9
10        for char in word1:
11            if char not in dic1:
12                dic1[char] = 1
13            else:
14                dic1[char] += 1
15
16        for char in word2:
17            if char not in dic2:
18                dic2[char] = 1
19            else:
20                dic2[char] +=1
21        
22        # Condition 1: Must have the exact same set of unique characters
23        if set(dic1.keys()) != set(dic2.keys()):
24            return False
25        
26        # Condition 2: Must have the exact same collection of frequency counts
27        if sorted(dic1.values()) != sorted(dic2.values()):
28            return False
29        
30        return True