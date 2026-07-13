# Last updated: 7/13/2026, 4:48:30 PM
1from collections import defaultdict
2
3class Solution:
4    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
5        graph = defaultdict(dict)
6
7        for (u,v), val in zip(equations, values):
8            graph[u][v] = val
9            graph[v][u] = 1.0/val
10
11        def dfs(current_node,target_node,visited):
12            if current_node == target_node:
13                return 1.0
14
15            visited.add(current_node)
16
17            for neighbour, weight in graph[current_node].items():
18                if neighbour not in visited:
19                    product = dfs(neighbour,target_node,visited)
20                    if product != -1.0:
21                        return weight * product
22                
23            return -1.0
24
25        
26        results = []
27        for c,d in queries:
28            if c not in graph or d not in graph:
29                results.append(-1.0)
30            else:
31                visited = set()
32                results.append(dfs(c,d,visited))
33        
34        return results