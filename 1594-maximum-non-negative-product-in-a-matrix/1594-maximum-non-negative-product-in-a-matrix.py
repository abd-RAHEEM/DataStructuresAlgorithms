class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        maxProd = [[0]*n for _ in range(m)]
        minProd = [[0]*n for _ in range(m)]
        
        maxProd[0][0] = minProd[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, n):
            maxProd[0][j] = minProd[0][j] = maxProd[0][j-1] * grid[0][j]
        
        # Fill first column
        for i in range(1, m):
            maxProd[i][0] = minProd[i][0] = maxProd[i-1][0] * grid[i][0]
        
        # Fill rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                candidates = [
                    val * maxProd[i-1][j], val * minProd[i-1][j],
                    val * maxProd[i][j-1], val * minProd[i][j-1]
                ]
                maxProd[i][j] = max(candidates)
                minProd[i][j] = min(candidates)
        
        result = maxProd[m-1][n-1]
        return result % MOD if result >= 0 else -1
