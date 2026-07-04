class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj={i:[] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append((v,t))
        
        visited=[False]*(n+1)
        shortest=[float('inf')]*(n+1)
        shortest[0]=0
        shortest[k]=0
        time=0
        if adj[k]==[]:
            return -1
        q=[[0,k]]
        while q:
            cur_time,node=heapq.heappop(q)
            if cur_time>shortest[node]:
                continue
            for neigh,tm in adj[node]:
                new_t=cur_time+tm
                if new_t<shortest[neigh]:
                    shortest[neigh]=new_t
                    heapq.heappush(q,[new_t,neigh])
    

        time=max(shortest)
        return time if time!=float('inf') else -1