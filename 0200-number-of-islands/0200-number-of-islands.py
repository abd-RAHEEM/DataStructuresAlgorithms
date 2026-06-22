class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()
        queue=deque()
        m=len(grid)
        n=len(grid[0])
        island=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    visited.add((i,j))
                    queue.append([i,j])
                    while queue:
                        dr,dc=queue.popleft()
                        for r,c in directions:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1' and (nr,nc) not in visited:
                                visited.add((nr,nc))
                                queue.append([nr,nc])
                    island+=1
                else:
                    continue
        return island


        