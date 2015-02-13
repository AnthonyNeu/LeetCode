"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[0 for _ in range(n)]for _ in range(m)]
        
        # initialize
        d[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i-1][0] == 1:
                d[i][0] = 0
            else:
                d[i][0] = d[i-1][0]
                
        for i in range(1,n):
            if obstacleGrid[0][i-1] == 1:
                d[0][i] = 0
            else:
                d[0][i] = d[0][i-1]
          
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = (1 - obstacleGrid[i][j-1]) * d[i][j-1] + (1 - obstacleGrid[i-1][j]) * d[i-1][j]
        
        return d[m-1][n-1] * (1 - obstacleGrid[m-1][n-1])

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        ways[i][j] = 1
                    elif i == 0:
                        ways[i][j] = ways[i][j - 1]
                    elif j == 0:
                        ways[i][j] = ways[i - 1][j]
                    else:
                        ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]