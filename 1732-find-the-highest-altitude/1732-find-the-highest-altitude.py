class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt = 0
        current_alt = 0
        
        for g in gain:
            current_alt += g
            if current_alt > max_alt:
                max_alt = current_alt
                
        return max_alt
            