"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.column = [False] * n
        self.main_diag = [False] * 2 * n
        self.anti_diag = [False] * 2 * n
        self.result = []
        solution = []
        self.sloveNQueensRe(0,[],n)
        return self.result
        
    def sloveNQueensRe(self,row,solution,n):
        if row == n:
            self.result.append(map(lambda x: '.' * x + 'Q' + (n - x - 1) * '.',solution))
        else:
            for i in xrange(n):
                if self.column[i] is False and self.main_diag[row+i] is False and self.anti_diag[row-i+n] is False:
                    self.column[i] = self.main_diag[row+i] = self.anti_diag[row-i+n] = True
                    self.sloveNQueensRe(row+1,solution+[i],n)
                    self.column[i] = self.main_diag[row+i] = self.anti_diag[row-i+n] = False