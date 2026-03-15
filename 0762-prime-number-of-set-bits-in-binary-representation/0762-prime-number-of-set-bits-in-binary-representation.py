class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
    # Precompute prime set sizes we care about
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        def set_bits(n):
            return bin(n).count("1")
        
        count = 0
        for num in range(left, right + 1):
            if set_bits(num) in primes:
                count += 1
        return count
