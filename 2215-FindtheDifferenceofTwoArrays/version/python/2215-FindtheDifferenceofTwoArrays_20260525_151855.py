# Last updated: 5/25/2026, 3:18:55 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        dic = {}
4        for i in arr:
5            if i not in dic:
6                dic[i] = 1
7            else:
8                dic[i] += 1
9        
10        return len(dic.values()) == len(set(dic.values()))
11
12