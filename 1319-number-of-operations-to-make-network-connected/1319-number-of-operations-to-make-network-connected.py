class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<(n-1):
            return -1
        adj={i:[] for i in range(n)}
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        components=0
        def dfs(node):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        for i in range(n):
            if i not in visited:
                components+=1
                visited.add(i)
                dfs(i)
        return components-1
        