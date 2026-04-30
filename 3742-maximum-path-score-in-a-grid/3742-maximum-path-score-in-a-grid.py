class Solution(object):
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table with -1 (unreachable)
        # dp[i][j] stores a dictionary {cost: max_score} 
        # using a dict helps handle sparsity if k is much larger than actual paths
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        # Base case: Starting cell (0, 0)
        start_val = grid[0][0]
        start_cost = 0 if start_val == 0 else 1
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_val
        else:
            return -1

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue
                
                for current_cost, current_score in dp[i][j].items():
                    # Move Right and Down
                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        
                        if ni < m and nj < n:
                            val = grid[ni][nj]
                            next_cost = current_cost + (0 if val == 0 else 1)
                            next_score = current_score + val
                            
                            if next_cost <= k:
                                # Update if this is a better score for this specific cost
                                if next_score > dp[ni][nj].get(next_cost, -1):
                                    dp[ni][nj][next_cost] = next_score
        
        # Find the best score at the destination
        final_scores = dp[m-1][n-1].values()
        return max(final_scores) if final_scores else -1