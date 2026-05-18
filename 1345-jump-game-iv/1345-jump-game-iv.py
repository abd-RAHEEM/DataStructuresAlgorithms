from collections import deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Map each value to a list of its indices
        graph = {}
        for i, val in enumerate(arr):
            if val not in graph:
                graph[val] = []
            graph[val].append(i)
            
        # Queue stores tuples of (current_index, steps_taken)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            node, steps = queue.popleft()
            
            # If we reached the last index, return the number of steps
            if node == n - 1:
                return steps
            
            # Explore all possible next jumps
            neighbors = graph.get(arr[node], [])
            neighbors.append(node - 1)
            neighbors.append(node + 1)
            
            for child in neighbors:
                if 0 <= child < n and child not in visited:
                    visited.add(child)
                    queue.append((child, steps + 1))
            
            # CRITICAL OPTIMIZATION: Clear the list of indices for this value
            # so we don't process them again, preventing Time Limit Exceeded (TLE).
            if arr[node] in graph:
                del graph[arr[node]]
                
        return -1