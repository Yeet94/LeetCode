# Last updated: 7/27/2026, 4:13:57 PM
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        minutes = 0

        while queue and fresh_count > 0:
            level_size = len(queue)

            for _ in range(level_size):
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr = dr+r
                    nc = dc+c

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -=1
                        queue.append((nr,nc))
            
            minutes +=1
        

        return minutes if fresh_count == 0 else -1