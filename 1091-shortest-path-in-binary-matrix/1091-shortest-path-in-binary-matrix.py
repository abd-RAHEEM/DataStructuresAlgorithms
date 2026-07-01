class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        if n==1:
            return 1
        dist=[[float('inf')]*n for _ in range(n)]
        dist[0][0]=0
        q=deque([(0,0,1)])
        directions=[
            (-1,-1),(-1,0),(-1,1),
            (0,-1),(0,1)
            ,(1,-1),(1,0),(1,1)
        ]
        while q:
            r,c,pt=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (0<=nr<n and 0<=nc<n) and grid[nr][nc]==0 and pt+1<dist[nr][nc]:
                    dist[nr][nc]=pt+1
                    if nr==n-1 and nc==n-1:
                        return pt+1
                    q.append((nr,nc,pt+1))
        return -1
        