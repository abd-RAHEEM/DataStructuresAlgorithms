class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Special case: if n = 0, complement is 1
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
