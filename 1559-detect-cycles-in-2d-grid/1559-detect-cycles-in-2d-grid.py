class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, char):
            visited.add((r, c))
            
            # Directions: Up, Down, Left, Right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the character matches
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    # If we find a visited cell that isn't the parent, a cycle exists
                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
                        return True
                    # If not visited, continue DFS
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c, char):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Start DFS; parent of the start node is set to -1, -1
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        
        return False