class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # 1. Calculate Prefix Maximums from left to right
        prefix_max = [0] * n
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            prefix_max[i] = curr_max
            
        # 2. Calculate Suffix Minimums from right to left
        suffix_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffix_min[i] = curr_min
            
        ans = [0] * n
        # 3. Identify components. A split occurs where 
        # prefix_max[i] <= suffix_min[i+1]
        start = 0
        while start < n:
            end = start
            max_in_component = nums[start]
            
            # Expand the component until the "cut" condition is met
            while end < n - 1 and prefix_max[end] > suffix_min[end + 1]:
                end += 1
                max_in_component = max(max_in_component, nums[end])
            
            # Re-verify the max for the identified range
            # (The prefix_max logic already helps, but let's be explicit)
            component_max = prefix_max[end]
            
            for k in range(start, end + 1):
                ans[k] = component_max
            
            start = end + 1
            
        return ans