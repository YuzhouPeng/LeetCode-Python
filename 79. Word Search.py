direction = [[1,0],[-1,0],[0,1],[0,-1]]
def backtracking(curlen,r,c,visited,board,word,m,n):
    if curlen==len(word):
        return True
    if r<0 or r>=m or c<0 or c>=n or board[r][c]!=word[curlen] or visited[r][c]==1:
        return False
    visited[r][c] = 1
    for d in direction:
        if backtracking(curlen+1,r+d[0],c+d[1],visited,board,word,m,n):
            return True
    visited[r][c] = 0

    return False


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == None or len(word) == 0:
            return True
        if board == None or len(word) == 0 or len(board[0]) == 0:
            return False
        m = len(board)
        n = len(board[0])
        hasVistied = []
        for i in range(m):
            list1 = [0 for k in range(n)]
            hasVistied.append(list1)

        for r in range(m):
            for c in range(n):
                if backtracking(0,r,c,hasVistied,board,word,m,n):
                    return True

        return False

