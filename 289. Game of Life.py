neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]


def nnb(board, i, j):
    count = 0
    m, n = len(board), len(board[0])
    for d in neighbors:
        if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
            count += board[i + d[0]][j + d[1]] % 2
    return count


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                if board[i][j] == 0 or board[i][j] == 2:
                    if nnb(board, i, j) == 3:
                        board[i][j] = 2
                elif nnb(board, i, j) < 2 or nnb(board, i, j) > 3:
                    board[i][j] = 3
        for i in range(height):
            for j in range(width):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
        return board
