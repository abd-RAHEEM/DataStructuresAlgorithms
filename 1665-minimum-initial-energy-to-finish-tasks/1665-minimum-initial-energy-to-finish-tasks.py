class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort tasks by the difference between minimum and actual energy descending
        # (minimum - actual) represents the "saved" energy requirement
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        current_energy = 0
        total_initial_energy = 0
        
        for actual, minimum in tasks:
            # If current energy is less than what's required to start the task
            if current_energy < minimum:
                # Add the deficit to our total starting energy
                total_initial_energy += (minimum - current_energy)
                # After "refilling", our energy becomes exactly the minimum required
                current_energy = minimum
            
            # Spend the actual energy required for the task
            current_energy -= actual
            
        return total_initial_energy