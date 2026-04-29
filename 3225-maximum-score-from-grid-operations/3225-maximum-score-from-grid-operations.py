class Solution(object):
    def maximumScore(self, grid):
        n = len(grid)
        # Precompute prefix sums for each column for O(1) range sum queries
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]

        # dp[h] stores the max score for the current column at height h
        # We use two DP arrays to handle the 'increasing' and 'decreasing' logic
        # inc[h]: max score ending at column j with height h, where height is increasing
        # dec[h]: max score ending at column j with height h, where height is decreasing
        inc = [0] * (n + 1)
        dec = [0] * (n + 1)

        for j in range(1, n):
            next_inc = [0] * (n + 1)
            next_dec = [0] * (n + 1)
            
            # Case 1: Column height is increasing (h > prev_h)
            # You gain points from column j-1 that are above prev_h but below h
            max_prev = 0
            for h in range(n + 1):
                next_inc[h] = max(next_inc[h], max_prev)
                max_prev = max(max_prev, inc[h] - pref[j-1][h])
                next_inc[h] += pref[j-1][h]

            # Case 2: Column height is decreasing (h < prev_h)
            # You gain points from column j that are above h but below prev_h
            max_prev = 0
            for h in range(n, -1, -1):
                max_prev = max(max_prev, max(inc[h], dec[h]) + pref[j][h])
                next_dec[h] = max(next_dec[h], max_prev - pref[j][h])

            # Case 3: Transition from decreasing to increasing (valley shape)
            # If we were decreasing and now we increase, we can reset from the best dec state
            best_dec = max(dec)
            for h in range(n + 1):
                next_inc[h] = max(next_inc[h], best_dec)

            inc, dec = next_inc, next_dec

        return max(max(inc), max(dec))