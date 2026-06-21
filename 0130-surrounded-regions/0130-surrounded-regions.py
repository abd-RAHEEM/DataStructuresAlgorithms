class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        queue=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        board[i][j]='S'
                        queue.append((i,j))
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=dr+r,c+dc
                if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O':
                    board[nr][nc]='S'
                    queue.append((nr,nc))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='S':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
                    
            
                    
                    
        
