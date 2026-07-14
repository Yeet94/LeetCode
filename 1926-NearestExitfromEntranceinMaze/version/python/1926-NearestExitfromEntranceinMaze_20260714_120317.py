# Last updated: 7/14/2026, 12:03:17 PM
1from collections import deque
2
3class Solution:
4    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
5        m = len(maze)
6        n = len(maze[0])
7
8        queue = deque([(entrance[0],entrance[1],0)])
9        
10        maze[entrance[0]][entrance[1]] = '+'
11
12        directions = [(-1,0),(1,0),(0,-1),(0,1)]    
13        
14        while queue:
15            row,col,cost = queue.popleft()
16            if (row == 0 or row == m-1 or col == 0 or col == n-1) and cost > 0:
17                return cost
18
19            for dr,dc in directions:
20                next_row = row + dr
21                next_col = col + dc
22
23                if 0 <= next_row < m and 0 <= next_col < n and maze[next_row][next_col] == '.':
24                    maze[next_row][next_col] = '+'
25                    queue.append((next_row,next_col,cost+1))
26        
27
28        return -1
29
30
31            