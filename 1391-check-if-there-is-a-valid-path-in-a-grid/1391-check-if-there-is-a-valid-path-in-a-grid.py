from collections import deque

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Mapping street types to allowed directions (row_offset, col_offset)
        # Directions: Up: (-1, 0), Down: (1, 0), Left: (0, -1), Right: (0, 1)
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            current_street = grid[r][c]
            
            for dr, dc in directions[current_street]:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if already visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    neighbor_street = grid[nr][nc]
                    
                    # Connection Check: Does the neighbor have a path back to (r, c)?
                    # If we moved by (dr, dc), the neighbor must have a path in (-dr, -dc)
                    if (-dr, -dc) in directions[neighbor_street]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False