class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        # Count the occurrences of each character
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_underscore = moves.count('_')
        
        # The furthest distance will be the absolute difference between L and R,
        # plus all the underscores moving in that dominant direction.
        return abs(count_L - count_R) + count_underscore