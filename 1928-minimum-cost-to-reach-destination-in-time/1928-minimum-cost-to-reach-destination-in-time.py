class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n=len(passingFees)
        adj={i:[] for i in range(n)}
        for u,v,tm in edges:
            adj[u].append((v,tm))
            adj[v].append((u,tm))
        minTime=[float('inf')]*n
        minTime[0]=0
        queue=[(passingFees[0],0,0)]
        while queue:
            fee,node,tm=heapq.heappop(queue)
            if node==n-1:
                return fee
            for neigh, t in adj[node]:
                if tm+t<=maxTime and tm+t<minTime[neigh]:
                    minTime[neigh]=tm+t
                    heapq.heappush(queue,(passingFees[neigh]+fee,neigh,minTime[neigh]))
        return -1
        