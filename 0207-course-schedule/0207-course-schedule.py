class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap={i:[] for i in range(numCourses)}
        for i, adj in prerequisites:
            premap[i].append(adj)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs]==[]:
                return True
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            premap[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        