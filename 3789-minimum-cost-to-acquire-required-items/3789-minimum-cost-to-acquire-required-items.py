class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """

        cost=0
        k=min(need1,need2)
        one_unit=min(costBoth,cost1+cost2)
        cost+=k*one_unit
        need1-=k
        need2-=k
        if need1!=0:
            unit=min(costBoth,cost1)
            cost+=need1*unit
        elif need2!=0:
            unit=min(costBoth,cost2)
            cost+=need2*unit
        return cost
        