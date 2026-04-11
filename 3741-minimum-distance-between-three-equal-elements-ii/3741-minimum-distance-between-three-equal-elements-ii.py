class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        indices = defaultdict(list)
        for i, val in enumerate(nums):
            indices[val].append(i)
        
        min_dist = float('inf')
        
        for val in indices:
            idx_list = indices[val]
            if len(idx_list) >= 3:
                # Check every consecutive triplet of indices for this value
                for m in range(len(idx_list) - 2):
                    dist = 2 * (idx_list[m+2] - idx_list[m])
                    min_dist = min(min_dist, dist)
                    
        return min_dist if min_dist != float('inf') else -1