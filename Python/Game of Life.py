"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0: from dead to dead
        # 1: from live to live
        # 2: from dead to live
        # 3: from live to dead
        state_table = {0: 0, 1: 1, 2: 1, 3: 0}
        if not board or len(board[0]) == 0:
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    state = self.calculateSum(board, i, j)
                    if state == 3:
                        board[i][j] = 2
                elif board[i][j] == 1:
                    state = self.calculateSum(board, i, j)
                    if state < 2 or state > 3:
                        board[i][j] = 3
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = state_table[board[i][j]]
                    
                    
    def calculateSum(self, board, i, j):
        state = 0
        for ii, jj in (i - 1, j - 1), (i + 1, j + 1), (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1), (i + 1, j - 1), (i - 1, j + 1):
            if 0 <= ii < len(board) and 0 <= jj < len(board[0]):
                state += board[ii][jj] % 2
        return state
        #return sum(map(lambda x : board[x[0]][x[1]] % 2, filter(lambda x : 0 <= x[0] < len(board) and 0 <= x[1] < len(board[0]), [(i - 1, j - 1), (i + 1, j + 1), (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1), (i + 1, j - 1), (i - 1, j + 1)])))
        #return len([t for t in [(i - 1, j - 1), (i + 1, j + 1), (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1), (i + 1, j - 1), (i - 1, j + 1)] if 0 <= t[0] < len(board) and 0 <= t[1] < len(board[0]) and board[t[0]][t[1]] % 2])
