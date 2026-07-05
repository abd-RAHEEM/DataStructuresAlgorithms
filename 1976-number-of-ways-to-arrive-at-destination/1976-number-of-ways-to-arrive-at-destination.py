class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj={i:[] for i in range(n)}
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        dist=[float('inf')]*n
        ways=[1]*n
        q=[(0,0)]
        dist[0]=0
        while q:
            current_t, node=heapq.heappop(q)
            if current_t>dist[node]:
                continue
            
            for neigh, nt in adj[node]:
                if current_t+nt<dist[neigh]:
                    dist[neigh]=current_t+nt
                    ways[neigh]=ways[node]
                    heapq.heappush(q,(dist[neigh],neigh))
                elif current_t+nt==dist[neigh]:
                    ways[neigh]=(ways[neigh]+ways[node])% (10**9+7)
        return ways[n-1]
        