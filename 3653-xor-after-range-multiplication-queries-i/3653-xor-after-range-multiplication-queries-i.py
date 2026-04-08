class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """

        MOD = 10**9 + 7
        
        # Process each query
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
        
        # Compute XOR of all elements
        result = 0
        for num in nums:
            result ^= num
        return result


