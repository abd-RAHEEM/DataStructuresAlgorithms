from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_len = 0
        
        # Handle the special case of 1s
        if 1 in counts:
            c = counts[1]
            max_len = c if c % 2 != 0 else c - 1
            
        # Process other numbers
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            # Keep building the chain as long as we have at least 2 copies 
            # and the next square exists in the array
            while curr in counts and counts[curr] >= 2 and (curr * curr) in counts:
                current_len += 2
                curr = curr * curr
            
            # The final element in the chain acts as the single peak element
            if curr in counts:
                current_len += 1
            else:
                # If the last element doesn't exist, we must backtrack 
                # because the previous element cannot be the peak if it was already split
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len