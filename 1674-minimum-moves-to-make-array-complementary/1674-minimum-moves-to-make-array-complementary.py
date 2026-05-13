class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # Difference array to track moves for each possible sum T from 2 to 2*limit
        # diff[i] stores the change in moves at sum i
        diff = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Standardize so a is the smaller value
            v1, v2 = min(a, b), max(a, b)
            
            # 1. Default: 2 moves for all possible sums [2, 2 * limit]
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # 2. Reduced to 1 move: 
            # If target sum is in [v1 + 1, v2 + limit], we only need 1 move.
            # We subtract 1 from the "2 moves" we added above.
            diff[v1 + 1] -= 1
            diff[v2 + limit + 1] += 1
            
            # 3. Reduced to 0 moves:
            # If target sum is exactly v1 + v2, we need 0 moves.
            # We subtract 1 more from the "1 move" range at this specific point.
            diff[v1 + v2] -= 1
            diff[v1 + v2 + 1] += 1
            
        ans = n
        current_moves = 0
        # Sweep through the difference array to find the minimum moves
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            ans = min(ans, current_moves)
            
        return ans