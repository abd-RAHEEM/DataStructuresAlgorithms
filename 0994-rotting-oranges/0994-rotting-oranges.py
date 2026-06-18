class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        fresh_count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh_count+=1
        
        if fresh_count==0:
            return 0

        minutes=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while queue and fresh_count>0:
            minutes+=1

            for _ in range(len(queue)):
                r,c=queue.popleft()

                for dr,dc in directions:
                    nr,nc=dr+r, dc+c
                    if 0<=nr< rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_count-=1
                        queue.append((nr,nc))

        return minutes if fresh_count==0 else -1