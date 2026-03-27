class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            row = mat[i]
            if i % 2 == 0:  # even row → left shift
                shifted = row[k % n:] + row[:k % n]
            else:           # odd row → right shift
                shifted = row[-(k % n):] + row[:-(k % n)]
            
            if shifted != row:
                return False
        return True
