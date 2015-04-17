"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def totalNQueens(self, n):
        self.column = [False] * n
        self.main_diag = [False] * 2 * n
        self.anti_diag = [False] * 2 * n
        return self.totalNQueensRe(0,[],n)
        
    def totalNQueensRe(self,row,solution,n):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            if self.column[i] is False and self.main_diag[row+i] is False and self.anti_diag[row-i+n] is False:
                self.column[i] = self.main_diag[row+i] = self.anti_diag[row-i+n] = True
                result += self.totalNQueensRe(row+1,solution+[i],n)
                self.column[i] = self.main_diag[row+i] = self.anti_diag[row-i+n] = False
        return result
