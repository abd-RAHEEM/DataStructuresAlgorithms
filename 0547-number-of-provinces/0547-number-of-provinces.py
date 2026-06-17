class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        v=len(isConnected)
        visited=set()

        def dfs(city):
            visited.add(city)

            for neighbor in range(v):
                if isConnected[city][neighbor]==1 and neighbor not in visited:
                    dfs(neighbor)
        province=0
        for i in range(v):
            if i not in visited:
                province+=1
                dfs(i)
        return province
