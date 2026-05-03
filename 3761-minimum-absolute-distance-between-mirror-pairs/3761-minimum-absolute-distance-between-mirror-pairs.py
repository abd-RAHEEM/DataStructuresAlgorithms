class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_reverse(n):
            # int() automatically handles leading zeros, e.g., int("021") -> 21
            return int(str(n)[::-1])
        
        # Maps the REVERSE of a seen number to its original index
        # key: reverse(nums[i]), value: i
        reverse_map = {}
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            # If the current value matches a reverse we've stored, we found a pair
            if val in reverse_map:
                min_dist = min(min_dist, j - reverse_map[val])
            
            # Store the reverse of the current number to be found by a future nums[j]
            target = get_reverse(val)
            reverse_map[target] = j
            
        return min_dist if min_dist != float('inf') else -1