# Last updated: 7/27/2026, 4:13:43 PM
from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}

        for u,v in connections:
                
            if u not in graph:
                graph[u] = []
            graph[u].append((v,1))
            
            if v not in graph:
                graph[v] = []
            graph[v].append((u,0))


        changes= 0
        visited = {0}
        queue = deque([0])


        while queue:
            curr = queue.popleft()

            for neighbour, is_original in graph.get(curr,[]):
                if neighbour not in visited:
                    if is_original == 1:
                        changes +=1
                    visited.add(neighbour)
                    queue.append(neighbour)

        return changes
