class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        queue=deque()
        m=len(grid)
        count=0
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and ( i==0 or i==m-1 or j==0 or j==n-1):
                    queue.append([i,j])
                    grid[i][j]=2
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and  grid[nr][nc]==1:
                    grid[nr][nc]=2
                    queue.append([nr,nc])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    grid[i][j]=1
                elif grid[i][j]==1:
                    count+=1
                else:
                    continue
        return count