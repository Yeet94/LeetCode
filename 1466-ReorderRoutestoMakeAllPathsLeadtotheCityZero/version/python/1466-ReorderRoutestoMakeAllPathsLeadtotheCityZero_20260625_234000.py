# Last updated: 6/25/2026, 11:40:00 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        num_cities = len(isConnected)
4        parent = [i for i in range(num_cities)]
5        provinces = num_cities
6
7        def find(i):
8            if parent[i] == i:
9                return i
10            parent[i] = find(parent[i])
11            return parent[i]
12
13        def union(i,j):
14            nonlocal provinces
15            root_i = find(i)
16            root_j = find(j)
17
18            if root_i != root_j:
19                parent[root_i] = root_j
20                provinces -=1
21
22        for i in range(num_cities):
23            for j in range(i+1,num_cities):
24                if isConnected[i][j] == 1:
25                    union(i,j)
26
27        return provinces        
28            