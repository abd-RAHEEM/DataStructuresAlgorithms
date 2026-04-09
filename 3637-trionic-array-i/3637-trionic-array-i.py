class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        n = len(nums)
        if n < 4:  # Minimum length to have 0 < p < q < n-1
            return False
        
        i = 0
        
        # 1. Strictly Increasing: nums[0...p]
        # Must move at least one step (p > 0)
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        
        p = i
        if p == 0 or p == n - 1:
            return False
            
        # 2. Strictly Decreasing: nums[p...q]
        # Must move at least one step (q > p)
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            
        q = i
        if q == p or q == n - 1:
            return False
            
        # 3. Strictly Increasing: nums[q...n-1]
        # Must move at least one step and reach the end
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # If we reached the last index, it's a valid Trionic array
        return i == n - 1