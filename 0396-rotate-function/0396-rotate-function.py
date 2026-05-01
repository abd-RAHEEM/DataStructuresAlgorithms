class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        
        # Calculate F(0)
        current_f = 0
        for i in range(n):
            current_f += i * nums[i]
            
        max_f = current_f
        
        # Iteratively calculate F(1) to F(n-1) using the derived formula
        # F(k) = F(k-1) + total_sum - n * nums[n-k]
        for k in range(1, n):
            current_f = current_f + total_sum - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f