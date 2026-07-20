class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(grid)
        n=len(grid[0])
        total=n*m
        k=k%total
        result=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                index=i*n+j
                new_index=(index+k)%total
                new_row=new_index//n
                new_col=new_index%n
                result[new_row][new_col]=grid[i][j]
        return result