class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Sort costs in descending order to prioritize paying for expensive ones
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the array
        for i in range(len(cost)):
            # If the index is not a multiple of 3, add the cost.
            # (Indices 0, 1 are paid, 2 is skipped, 3, 4 are paid, 5 is skipped...)
            if i % 3 != 2:
                total_cost += cost[i]
                
        return total_cost