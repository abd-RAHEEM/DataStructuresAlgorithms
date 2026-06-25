class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        preq={i:[] for i in range(numCourses)}
        for crs, pr in prerequisites:
            preq[crs].append(pr)
        visited=set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if preq[crs]==[]:
                if crs in result:
                    return True
                result.append(crs)
                return True
            visited.add(crs)
            for pre in preq[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preq[crs]=[]
            result.append(crs)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return result