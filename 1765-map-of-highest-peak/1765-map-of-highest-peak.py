class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(isWater)
        n=len(isWater[0])
        queue=deque()
        height=[[-1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    height[i][j]=0
                    queue.append((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and height[nr][nc]==-1:
                    height[nr][nc]=height[r][c]+1
                    queue.append((nr,nc))
        return height
