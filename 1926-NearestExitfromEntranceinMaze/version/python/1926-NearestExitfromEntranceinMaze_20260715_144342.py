# Last updated: 7/15/2026, 2:43:42 PM
1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        m = len(grid)
5        n = len(grid[0])
6        queue = deque()
7        directions = [(-1,0),(1,0),(0,-1),(0,1)]
8
9        fresh_count = 0
10        for r in range(m):
11            for c in range(n):
12                if grid[r][c] == 1:
13                    fresh_count += 1
14                elif grid[r][c] == 2:
15                    queue.append((r,c))
16        
17        minutes = 0
18
19        while queue and fresh_count > 0:
20            level_size = len(queue)
21
22            for _ in range(level_size):
23                r,c = queue.popleft()
24
25                for dr, dc in directions:
26                    nr = dr+r
27                    nc = dc+c
28
29                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
30                        grid[nr][nc] = 2
31                        fresh_count -=1
32                        queue.append((nr,nc))
33            
34            minutes +=1
35        
36
37        return minutes if fresh_count == 0 else -1