# Last updated: 8/27/2026, 11:38:10 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        
13        if not node:
14            return None
15
16        visited = {}
17
18        def dfs(curr : 'Node') -> 'Node':
19            if curr in visited:
20                return visited[curr]
21        
22            clone = Node(curr.val)
23            visited[curr] = clone
24
25            for neighbor in curr.neighbors:
26                clone_neighbor = dfs(neighbor)
27                clone.neighbors.append(clone_neighbor)
28            return clone
29        
30        return dfs(node)