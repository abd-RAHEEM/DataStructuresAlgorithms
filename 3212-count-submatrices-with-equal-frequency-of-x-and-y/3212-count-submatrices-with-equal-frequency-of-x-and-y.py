class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        prefixX = [[0]*(n+1) for _ in range(m+1)]
        prefixY = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                prefixX[i+1][j+1] = prefixX[i+1][j] + prefixX[i][j+1] - prefixX[i][j] + (1 if grid[i][j] == 'X' else 0)
                prefixY[i+1][j+1] = prefixY[i+1][j] + prefixY[i][j+1] - prefixY[i][j] + (1 if grid[i][j] == 'Y' else 0)

        ans = 0
        for i in range(m):
            for j in range(n):
                countX = prefixX[i+1][j+1]
                countY = prefixY[i+1][j+1]
                if countX == countY and countX > 0:
                    ans += 1
        return ans
