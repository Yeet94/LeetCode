# Last updated: 7/27/2026, 4:13:36 PM
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        queue = deque([(entrance[0],entrance[1],0)])
        
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(-1,0),(1,0),(0,-1),(0,1)]    
        
        while queue:
            row,col,cost = queue.popleft()
            if (row == 0 or row == m-1 or col == 0 or col == n-1) and cost > 0:
                return cost

            for dr,dc in directions:
                next_row = row + dr
                next_col = col + dc

                if 0 <= next_row < m and 0 <= next_col < n and maze[next_row][next_col] == '.':
                    maze[next_row][next_col] = '+'
                    queue.append((next_row,next_col,cost+1))
        

        return -1


            