class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = float('inf')
        
        for num in nums:
            digit_sum = 0
            # Calculate the sum of digits using modulo and division
            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            # Keep track of the minimum digit sum encountered
            if digit_sum < min_sum:
                min_sum = digit_sum
                
        return min_sum