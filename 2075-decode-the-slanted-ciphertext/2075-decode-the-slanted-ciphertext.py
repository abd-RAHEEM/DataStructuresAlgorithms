class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        n = len(encodedText)
        cols = n // rows
        # Build matrix row-wise
        matrix = [encodedText[i*cols:(i+1)*cols] for i in range(rows)]
        
        res = []
        # Traverse diagonally
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                res.append(matrix[r][c])
                r += 1
                c += 1
        
        return "".join(res).rstrip()
