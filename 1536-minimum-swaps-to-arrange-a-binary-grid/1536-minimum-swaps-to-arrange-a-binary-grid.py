class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Step 1: compute rightmost 1 in each row
        last_one = []
        for row in grid:
            pos = -1
            for j in range(n):
                if row[j] == 1:
                    pos = j
            last_one.append(pos)

        swaps = 0
        # Step 2: greedy placement
        for i in range(n):
            j = i
            while j < n and last_one[j] > i:
                j += 1
            if j == n:  # no valid row found
                return -1
            # bring row j up to i
            while j > i:
                last_one[j], last_one[j-1] = last_one[j-1], last_one[j]
                swaps += 1
                j -= 1
        return swaps



