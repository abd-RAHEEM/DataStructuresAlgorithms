class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        res = 0
        length = 0
        
        for x in range(1, n+1):
            # update length when x is a power of 2
            if (x & (x - 1)) == 0:
                length += 1
            res = ((res << length) + x) % MOD
        
        return res
