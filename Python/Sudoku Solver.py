"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

# BFS solution
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()
        
    def solve(self):
        for i in xrange(len(self.board)):
            for j in xrange(len(self.board)):
                if(self.board[i][j] == '.'):
                    for k in xrange(9):
                        self.board[i][j] = chr(ord('1') + k)
                        if self.isValid(i, j) and self.solve():
                            return True
                        self.board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, x, y):
        for i in xrange(9):
            if i != x and self.board[i][y] == self.board[x][y]:
                return False
            
        for j in xrange(9):
            if j != y and self.board[x][j] == self.board[x][y]:
                return False
            
        i = 3 * (x / 3)
        while i < 3 * (x / 3 + 1):
            j = 3 * (y / 3)
            while j < 3 * (y / 3 + 1):
                if (i != x or j != y) and self.board[i][j] == self.board[x][y]:
                    return False
                j += 1
            i += 1
            
        return True