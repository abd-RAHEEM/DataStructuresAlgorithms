class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        starting=image[sr][sc]
        row,col=len(image),len(image[0])
        if image[sr][sc]==color:
            return image
        queue=deque()
        queue.append((sr,sc))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c=queue.popleft()
            if image[r][c]==starting:
                image[r][c]=color
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and image[nr][nc]==starting:
                        queue.append((nr,nc))
        return image
