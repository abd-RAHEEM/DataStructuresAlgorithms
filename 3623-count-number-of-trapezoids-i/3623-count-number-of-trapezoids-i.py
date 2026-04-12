class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Group points by their y-coordinate
        y_map = {}
        for x, y in points:
            y_map[y] = y_map.get(y, 0) + 1
            
        # Step 2: Calculate the number of possible horizontal segments at each y-level
        # A segment needs 2 points: comb(k, 2) = k * (k-1) // 2
        segments_per_level = []
        for y in y_map:
            k = y_map[y]
            if k >= 2:
                segments = (k * (k - 1)) // 2
                segments_per_level.append(segments)
        
        # Step 3: Count combinations of segments from different levels
        # Total = Sum of (segments[i] * segments[j]) for all i < j
        total_trapezoids = 0
        prefix_sum = 0
        
        for s in segments_per_level:
            # Multiply current segments by the sum of all segments seen so far
            total_trapezoids = (total_trapezoids + s * prefix_sum) % MOD
            # Update prefix_sum for the next iteration
            prefix_sum = (prefix_sum + s) % MOD
            
        return total_trapezoids