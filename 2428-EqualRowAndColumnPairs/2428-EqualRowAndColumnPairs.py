# Last updated: 7/27/2026, 4:13:33 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_map = {}
        
        for row in grid:
            row_tuple = tuple(row)
        
            if row_tuple not in rows_map:
                rows_map[row_tuple] = 1
            else:
                rows_map[row_tuple] += 1

        total_pairs = 0

        for c in range(len(grid)):
            current_col = []
            for r in range(len(grid)):
                current_col.append(grid[r][c])
            
            col_tuple = tuple(current_col)    
        
            if col_tuple in rows_map:
                total_pairs += rows_map[col_tuple]

        return total_pairs
        
        