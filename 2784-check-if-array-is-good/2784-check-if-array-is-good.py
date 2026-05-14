class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The length of the array must be n + 1
        # If n is the max element, then n = len(nums) - 1
        n = len(nums) - 1
        
        # Base case for n < 1 (though constraints say nums.length >= 1)
        if n < 1:
            return False
            
        # Count the occurrences of each number
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
            
        # Check numbers from 1 to n-1
        for i in range(1, n):
            if counts.get(i) != 1:
                return False
                
        # Check if n appears exactly twice
        return counts.get(n) == 2