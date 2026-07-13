class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[float('inf')]*n for i in range(m)]
        minsum=None
        dp[0][0]=grid[0][0]
        for i in range(1):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+grid[i][j]
        for i in range(1,m):
            for j in range(1):
                dp[i][j]=dp[i-1][j]+grid[i][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
        