class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert n to string, reverse it, and convert back to integer
        reversed_n = int(str(n)[::-1])
        
        # Calculate and return the absolute difference
        return abs(n - reversed_n)