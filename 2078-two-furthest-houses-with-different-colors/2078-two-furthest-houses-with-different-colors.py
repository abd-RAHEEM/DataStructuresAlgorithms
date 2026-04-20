class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        max_dist = 0
        
        # Case 1: Compare everything with the first house
        # Look for the last house that doesn't match colors[0]
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
        
        # Case 2: Compare everything with the last house
        # Look for the first house that doesn't match colors[n-1]
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist