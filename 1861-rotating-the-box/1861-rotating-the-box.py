class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Apply gravity to each row
        for row in boxGrid:
            # pointer for the rightmost available empty cell
            empty_pos = n - 1 
            for c in range(n - 1, -1, -1):
                if row[c] == "*":
                    # Obstacle resets the potential landing spot
                    empty_pos = c - 1
                elif row[c] == "#":
                    # Swap stone to the empty position
                    row[c], row[empty_pos] = row[empty_pos], row[c]
                    empty_pos -= 1
        
        # Step 2: Rotate the matrix 90 degrees clockwise
        # Original (m x n) becomes (n x m)
        rotated_box = [["" for _ in range(m)] for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                rotated_box[c][m - 1 - r] = boxGrid[r][c]
                
        return rotated_box