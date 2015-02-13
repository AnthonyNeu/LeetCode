"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        
        d = [[0 for _ in range(n)]for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    d[i][j] = 1
                elif j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        
        return d[m-1][n-1]