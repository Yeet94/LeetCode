# Last updated: 7/27/2026, 4:14:15 PM
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (u,v), val in zip(equations,values):
            graph[u][v] = val
            graph[v][u] = 1.0/val

        def dfs(current_node, target_node, visited):
            if current_node == target_node:
                return 1.0
            
            visited.add(current_node)
            
            for neighbour,weight in graph[current_node].items():
                if neighbour not in visited:
                    product = dfs(neighbour,target_node,visited)
                    if product != -1.0:
                        return weight*product
            
            return -1.0

        
        results = []
        for c,d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                visited = set()
                results.append(dfs(c,d,visited))
        
        return results