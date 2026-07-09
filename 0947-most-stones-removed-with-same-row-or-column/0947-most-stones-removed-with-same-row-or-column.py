class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        rows=defaultdict(list)
        cols=defaultdict(list)

        for i, (r,c) in enumerate(stones):
            rows[r].append(i)
            cols[c].append(i)
        visited=[False ]*len(stones)
        def dfs(stone_idx):
            visited[stone_idx]=True
            r,c=stones[stone_idx]

            for neighbor in rows[r]:
                if not visited[neighbor]:
                    dfs(neighbor)
            for neighbor in cols[c]:
                if not visited[neighbor]:
                    dfs(neighbor)
        num_components=0
        for i in range(len(stones)):
            if not visited[i]:
                dfs(i)
                num_components+=1
        return len(stones)-num_components