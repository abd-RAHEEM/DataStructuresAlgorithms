class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heights = [[0]*n for _ in range(m)]
        
        # Build heights
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        
        max_area = 0
        for i in range(m):
            row = sorted(heights[i], reverse=True)
            for k, h in enumerate(row):
                max_area = max(max_area, h * (k+1))
        
        return max_area
