# Last updated: 5/8/2026, 4:22:42 PM
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Initialize DP table with -1 (meaning unreachable)
        # Dimensions: [rows][cols][cost_limit + 1]
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]

        #Base starting point
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):
                    #unreachable state can skip
                    if dp[i][j][c] == -1:
                        continue

                    current_score = dp[i][j][c]

                    #Right
                    ni,nj = i, j+1
                    #Boundary Check
                    if nj < n:
                        val = grid[ni][nj]
                        move_cost = 1 if val > 0 else 0
                        move_score = val
                        
                        next_cost = c + move_cost
                        if next_cost <= k:
                            # Update only if this new path is better than what we found before
                            if current_score + move_score > dp[ni][nj][next_cost]:
                                dp[ni][nj][next_cost] = current_score + move_score
                    
                    #Down
                    ni,nj = i+1, j
                    if ni < m:
                        val = grid[ni][nj]
                        move_cost = 1 if val>0 else 0
                        move_score = val

                        next_cost = c + move_cost
                        if next_cost <= k:
                            if current_score + move_score > dp[ni][nj][next_cost]:
                                dp[ni][nj][next_cost] = current_score + move_score
                    
        
        
        max_achievable_score = -1 
        for score in dp[m-1][n-1]:
            max_achievable_score = max(max_achievable_score, score)
        return max_achievable_score



