# Last updated: 6/25/2026, 11:38:41 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        num_cities = len(isConnected)
4        parent = [i for i in range(num_cities)]
5        provinces = num_cities
6
7
8        def find(i):
9            if parent[i] == i:
10                return i
11            parent[i] = find(parent[i])
12            return parent[i]
13       
14        def union(i,j):
15            nonlocal provinces
16            root_i = find(i)
17            root_j = find(j)
18
19
20            if root_i != root_j:
21                parent[root_i] = root_j
22                provinces -=1
23
24
25        for i in range(num_cities):
26            for j in range(i+1,num_cities):
27                if isConnected[i][j] == 1:
28                    union(i,j)
29
30
31        return provinces
32