class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            if num == target:
                # Calculate the distance from the start index
                current_dist = abs(i - start)
                
                # Update the minimum distance found so far
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return min_dist