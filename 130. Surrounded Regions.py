directions = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(board,r,c,m,n):
    if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O':
        return
    board[r][c]='T'
    for d in directions:
        dfs(board,r+d[0],c+d[1],m,n)
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if  board==None or len(board)==0:
            return

        m = len(board)
        n = len(board[0])
        for i in range(m):
            dfs(board,i,0,m,n)
            dfs(board,i,n-1,m,n)
        for i in range(n):
            dfs(board,0,i,m,n)
            dfs(board,m-1,i,m,n)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
