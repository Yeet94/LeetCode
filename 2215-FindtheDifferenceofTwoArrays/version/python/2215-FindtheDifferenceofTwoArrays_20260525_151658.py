# Last updated: 5/25/2026, 3:16:58 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        dic = {}
4        for i in arr:
5            if i not in dic:
6                dic[i] = 1
7            else:
8                dic[i] += 1
9        
10        count = []
11
12        for value in dic.values():
13            if value in count:
14                return False
15            else:
16                count.append(value)
17            
18        return True
19
20