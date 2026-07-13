class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range(m)]
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if (i==0 and j==0) or obstacleGrid[i][j]==1:
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                    continue
                if i>0:
                    dp[i][j]+=dp[i-1][j]
                if j>0:
                    dp[i][j]+=dp[i][j-1]
        return dp[m-1][n-1]