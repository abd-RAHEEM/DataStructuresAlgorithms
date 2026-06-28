class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        visited=[0]*len(graph)
        adj={i:[] for i in range(len(graph))}
        for node in range(len(graph)):
            for neigh in graph[node]:
                adj[node].append(neigh)
        result=[]
        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for neighbour in adj[node]:
                if not dfs(neighbour):
                    return False
            visited[node]=2
            return True
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
                
        return result