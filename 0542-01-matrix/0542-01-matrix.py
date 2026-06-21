class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        dist=[[-1] *n for _ in range(m)]
        queue=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    dist[i][j]=0
                    queue.append((i,j))
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r,c = queue.popleft()
            for i in range(len(directions)):
                nr,nc=r+directions[i][0],c+directions[i][1]
                if 0<=nr<m and 0<=nc<n and dist[nr][nc]==-1:
                    dist[nr][nc]=dist[r][c]+1
                    queue.append((nr,nc))
        return dist
