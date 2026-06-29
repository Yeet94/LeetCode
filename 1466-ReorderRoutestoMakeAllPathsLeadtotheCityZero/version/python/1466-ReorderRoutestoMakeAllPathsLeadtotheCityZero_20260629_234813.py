# Last updated: 6/29/2026, 11:48:13 PM
1from collections import deque
2
3class Solution:
4    def minReorder(self, n: int, connections: List[List[int]]) -> int:
5        graph = {}
6
7        for u,v in connections:
8                
9            if u not in graph:
10                graph[u] = []
11            graph[u].append((v,1))
12            
13            if v not in graph:
14                graph[v] = []
15            graph[v].append((u,0))
16
17
18        changes= 0
19        visited = {0}
20        queue = deque([0])
21
22
23        while queue:
24            curr = queue.popleft()
25
26            for neighbour, is_original in graph.get(curr,[]):
27                if neighbour not in visited:
28                    if is_original == 1:
29                        changes +=1
30                    visited.add(neighbour)
31                    queue.append(neighbour)
32
33        return changes
34