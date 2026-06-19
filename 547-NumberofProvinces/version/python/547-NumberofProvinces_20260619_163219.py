# Last updated: 6/19/2026, 4:32:19 PM
1from collections import deque
2
3class Solution:
4    def findCircleNum(self, isConnected: List[List[int]]) -> int:
5        num_cities = len(isConnected)
6        parent = [i for i in range(num_cities)]
7        provinces = num_cities
8
9        def find(i):
10            if parent[i] == i:
11                return i
12            parent[i] = find(parent[i])
13            return parent[i]
14        
15        def union(i,j):
16            nonlocal provinces
17            root_i = find(i)
18            root_j = find(j)
19
20            if root_i != root_j:
21                parent[root_i] = root_j
22                provinces -=1
23
24        for i in range(num_cities):
25            for j in range(i+1,num_cities):
26                if isConnected[i][j] == 1:
27                    union(i,j)
28
29        return provinces
30
31            