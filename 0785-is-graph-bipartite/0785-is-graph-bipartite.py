class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        color=[-1]*n
        for i in range(n):
            if color[i]==-1:
                queue=deque([i])
                color[i]=0

                while queue:
                    curr=queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor]==-1:
                            color[neighbor]=1-color[curr]
                            queue.append(neighbor)
                        elif color[neighbor]==color[curr]:
                            return False
        return True
        