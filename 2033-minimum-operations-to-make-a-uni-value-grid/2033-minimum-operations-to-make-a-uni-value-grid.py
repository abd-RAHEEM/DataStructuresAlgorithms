class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Flatten the 2D grid into a 1D list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # 1. Check if all elements have the same remainder modulo x
        remainder = nums[0] % x
        for val in nums:
            if val % x != remainder:
                return -1
        
        # 2. Sort the numbers to find the median
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        
        # 3. Sum the operations required to reach the median
        total_ops = 0
        for val in nums:
            total_ops += abs(val - median) // x
            
        return total_ops