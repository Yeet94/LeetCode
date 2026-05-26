# Last updated: 5/26/2026, 11:18:44 AM
1class Solution:
2    def equalPairs(self, grid: List[List[int]]) -> int:
3        rows_map = {}
4        
5        for row in grid:
6            row_tuple = tuple(row)
7        
8            if row_tuple not in rows_map:
9                rows_map[row_tuple] = 1
10            else:
11                rows_map[row_tuple] += 1
12
13        total_pairs = 0
14
15        for c in range(len(grid)):
16            current_col = []
17            for r in range(len(grid)):
18                current_col.append(grid[r][c])
19            
20            col_tuple = tuple(current_col)    
21        
22            if col_tuple in rows_map:
23                total_pairs += rows_map[col_tuple]
24
25        return total_pairs
26        
27        