class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m,n=len(grid),len(grid[0])
        skip=False
        result=[]
        for i in range(m):
            row= range(n) if i%2==0 else range(n-1,-1,-1)
            for j in row:
                if not skip:
                    result.append(grid[i][j])
                skip=not skip
        return result
