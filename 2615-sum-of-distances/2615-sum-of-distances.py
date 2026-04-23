from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        # Map each value to its list of indices
        indices_map = defaultdict(list)
        for i, val in enumerate(nums):
            indices_map[val].append(i)
        
        # Process each unique value's indices
        for val in indices_map:
            idxs = indices_map[val]
            k = len(idxs)
            
            # Calculate total sum of indices for this value to use in suffix calculations
            total_sum = sum(idxs)
            prefix_sum = 0
            
            for i, idx in enumerate(idxs):
                # i is the count of elements to the left
                # (k - 1 - i) is the count of elements to the right
                
                # Left side distances: (count * current_idx) - sum_of_left_indices
                left_val = (i * idx) - prefix_sum
                
                # Right side distances: sum_of_right_indices - (count * current_idx)
                suffix_sum = total_sum - prefix_sum - idx
                right_val = suffix_sum - ((k - 1 - i) * idx)
                
                res[idx] = left_val + right_val
                
                # Update prefix_sum for the next index in the list
                prefix_sum += idx
                
        return res