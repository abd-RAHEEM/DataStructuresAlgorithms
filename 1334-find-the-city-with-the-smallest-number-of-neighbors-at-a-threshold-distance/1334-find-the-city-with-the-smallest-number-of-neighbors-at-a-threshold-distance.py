class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        # 1. Initialize the distance matrix with infinity
        matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
            
        # 2. Populate the given edge weights
        for u, v, wt in edges:
            matrix[u][v] = wt
            matrix[v][u] = wt
            
        # 3. Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                        
        # 4. Count reachable cities and find the best one
        min_reachable = float('inf')
        best_city = -1
        
        for city in range(n):
            # Count how many cities are within the threshold from 'city'
            reachable_count = sum(1 for dist in matrix[city] if dist <= distanceThreshold)
            
            # Update if we find fewer neighbors, OR an equal number with a higher city ID
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                best_city = city
                
        return best_city