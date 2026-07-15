import collections
import bisect

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum / 2.0
        
        left_part = nums[:n]
        right_part = nums[n:]
        
        # 1. Recursive function to get all subset sums
        def get_subset_sums(arr):
            # Dictionary to store: { count_of_elements_picked : [list_of_sums] }
            res = collections.defaultdict(list)
            
            def dfs(idx, count, current_sum):
                # Base Case: If we've looked at all elements in this half
                if idx == len(arr):
                    res[count].append(current_sum)
                    return
                
                # Recursive Choice 1: Include the current element
                dfs(idx + 1, count + 1, current_sum + arr[idx])
                
                # Recursive Choice 2: Exclude the current element
                dfs(idx + 1, count, current_sum)
                
            dfs(0, 0, 0)
            return res

        # Generate all sums for left and right halves
        left_sums = get_subset_sums(left_part)
        right_sums = get_subset_sums(right_part)
        
        # Sort the right half sums so we can use Binary Search
        for k in range(n + 1):
            right_sums[k].sort()
            
        min_diff = float('inf')
        
        # 2. Meet in the middle
        for k in range(n + 1):
            # If we take k elements from left, we MUST take n-k from right
            needed_from_right = n - k
            
            for left_val in left_sums[k]:
                # We want: left_val + right_val = target
                # Therefore: right_val = target - left_val
                ideal_right_val = target - left_val
                
                # Binary search to find the closest available sum in the right half
                right_list = right_sums[needed_from_right]
                idx = bisect.bisect_left(right_list, ideal_right_val)
                
                # Check the value at idx (slightly larger or equal to ideal)
                if idx < len(right_list):
                    current_partition_sum = left_val + right_list[idx]
                    # formula: abs(total_sum - 2 * partition_sum)
                    diff = abs(total_sum - 2 * current_partition_sum)
                    min_diff = min(min_diff, diff)
                    
                # Check the value at idx - 1 (slightly smaller than ideal)
                if idx > 0:
                    current_partition_sum = left_val + right_list[idx - 1]
                    diff = abs(total_sum - 2 * current_partition_sum)
                    min_diff = min(min_diff, diff)
                    
        return int(min_diff)