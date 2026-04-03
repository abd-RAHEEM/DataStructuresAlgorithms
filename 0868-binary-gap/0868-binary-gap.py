class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert to binary string
        binary = bin(n)[2:]
        
        # Track positions of '1's
        ones_positions = [i for i, bit in enumerate(binary) if bit == '1']
        
        # If fewer than 2 ones, no gap
        if len(ones_positions) < 2:
            return 0
        
        # Compute max distance between consecutive ones
        max_gap = 0
        for i in range(1, len(ones_positions)):
            max_gap = max(max_gap, ones_positions[i] - ones_positions[i-1])
        
        return max_gap



