class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        prefix = stones[:]

        # Build prefix sums
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # If Alice takes all stones,
        # the game ends immediately.
        best = prefix[n - 1]

        # Try every earlier valid prefix
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best