class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        
        min_dist = float('inf')
        for indices in positions.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i+2] - indices[i])
                    min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1
