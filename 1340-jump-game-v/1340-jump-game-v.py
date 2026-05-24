class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = {}

        def dp(i):
            # Return cached result if already computed
            if i in memo:
                return memo[i]

            max_jumps = 1
            
            # Check jumps to the right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_jumps = max(max_jumps, 1 + dp(j))
                
            # Check jumps to the left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_jumps = max(max_jumps, 1 + dp(j))
                
            memo[i] = max_jumps
            return max_jumps

        # Start from every index and find the global maximum
        return max(dp(i) for i in range(n))