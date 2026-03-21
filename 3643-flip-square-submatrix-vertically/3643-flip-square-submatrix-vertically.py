class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Extract the submatrix
        submatrix = [row[y:y+k] for row in grid[x:x+k]]
        
        # Flip vertically (reverse rows)
        submatrix.reverse()
        
        # Put back into grid
        for i in range(k):
            grid[x+i][y:y+k] = submatrix[i]
        
        return grid
