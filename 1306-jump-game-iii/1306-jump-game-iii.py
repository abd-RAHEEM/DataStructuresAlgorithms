class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Base case: if we step out of bounds or reach an already visited index
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        
        # If we find an index with value 0, we've succeeded
        if arr[start] == 0:
            return True
        
        # Mark the current index as visited by making its value negative
        jump_distance = arr[start]
        arr[start] = -arr[start]
        
        # Recursively check jumping right (start + jump_distance) 
        # or jumping left (start - jump_distance)
        return (self.canReach(arr, start + jump_distance) or 
                self.canReach(arr, start - jump_distance))