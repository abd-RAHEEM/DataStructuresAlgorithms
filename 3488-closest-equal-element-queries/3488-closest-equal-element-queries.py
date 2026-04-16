import bisect
from collections import defaultdict

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Step 1: Map each value to a sorted list of its indices
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
            
        res = []
        for q_idx in queries:
            target_val = nums[q_idx]
            indices = val_to_indices[target_val]
            
            # If the element is unique, there are no "other" indices
            if len(indices) <= 1:
                res.append(-1)
                continue
            
            # Step 2: Find the position of the current index in the sorted list
            pos = bisect.bisect_left(indices, q_idx)
            
            # Step 3: Check neighbors (including circular wrap-around)
            # The candidates for the minimum distance are:
            # 1. The element to the immediate left
            # 2. The element to the immediate right
            # 3. The wrap-around distance (between first and last index)
            
            m = len(indices)
            
            # Left neighbor index (circular)
            left_idx = indices[(pos - 1) % m]
            dist_left = (q_idx - left_idx) if q_idx > left_idx else (q_idx + n - left_idx)
            
            # Right neighbor index (circular)
            right_idx = indices[(pos + 1) % m]
            dist_right = (right_idx - q_idx) if right_idx > q_idx else (right_idx + n - q_idx)
            
            res.append(min(dist_left, dist_right))
            
        return res