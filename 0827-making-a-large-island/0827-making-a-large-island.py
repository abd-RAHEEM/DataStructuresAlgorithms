class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        island_sizes = {}
        island_id = 2  # Start IDs from 2 since 0 and 1 are taken
        
        # Helper to perform iterative DFS and return the size of the island
        def get_island_size(start_r, start_c, current_id):
            stack = [(start_r, start_c)]
            grid[start_r][start_c] = current_id
            size = 0
            
            while stack:
                r, c = stack.pop()
                size += 1
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = current_id
                        stack.append((nr, nc))
            return size

        # Step 1: Scan the grid to label islands and map their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = get_island_size(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
                    
        # If there are no islands at all, flipping any 0 gives a size of 1
        # If the entire grid is one big island, return n * n
        max_size = max(island_sizes.values()) if island_sizes else 0
        if max_size == n * n:
            return n * n

        # Step 2: Evaluate flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_islands = set()
                    
                    # Check all 4 neighbors
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])
                    
                    # Potential size = 1 (the flipped 0 itself) + sum of distinct neighbor islands
                    potential_size = 1 + sum(island_sizes[i_id] for i_id in seen_islands)
                    max_size = max(max_size, potential_size)
                    
        return max_size