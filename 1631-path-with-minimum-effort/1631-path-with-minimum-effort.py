import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :type : int
        """
        m, n = len(heights), len(heights[0])
        
        # min-heap stores: (current_max_effort, r, c)
        min_heap = [(0, 0, 0)]
        
        # Track the minimum effort required to reach each cell
        effort_matrix = [[float('inf')] * n for _ in range(m)]
        effort_matrix[0][0] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            current_effort, r, c = heapq.heappop(min_heap)
            
            # If we reached the bottom-right cell, we found the minimum effort
            if r == m - 1 and c == n - 1:
                return current_effort
                
            # If we found a worse path to an already processed cell, skip it
            if current_effort > effort_matrix[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    # The effort to move to the neighbor is the max of the 
                    # effort so far and the absolute difference to the neighbor
                    new_effort = max(current_effort, abs(heights[r][c] - heights[nr][nc]))
                    
                    # If this path offers a lower effort to (nr, nc), update and push to heap
                    if new_effort < effort_matrix[nr][nc]:
                        effort_matrix[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
                        
        return 0