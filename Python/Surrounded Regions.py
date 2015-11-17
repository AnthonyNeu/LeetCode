"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M-1 or j == 0 or j == N-1:
                    self.bfs(board, i, j)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                
        
    def bfs(self, board, row, col):
        if (board[row][col] != 'O'):
            return
        q = []
        q.append((row, col))
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                continue
            if board[i][j] != 'O':
                continue
            board[i][j] = 'V'
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))

# pre-processing the point, start BFS from these points
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        current = []
        # only need to do bfs from the outer layer
        for i in xrange(len(board)):
            current.append((i, 0))
            current.append((i, len(board[0]) - 1))
        for i in xrange(len(board[0])):
            current.append((0, i))
            current.append((len(board) - 1, i))
            
        while current:
            i, j = current.pop()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                        board[x][y] = 'V'
                        current.append((x, y))
                        
        for i in xrange(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
