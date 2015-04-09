"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        M = len(grid)
        N = len(grid[0])
        
        island = [[False for _ in xrange(N)] for _ in xrange(M)]
        
        count = 0
        for i in xrange(M):
            for j in xrange(N):
                if island[i][j] == False and grid[i][j] == '1':
                    count +=1
                    island[i][j] = True
                    self.markIsland(grid,island,i,j)
                    
        return count
        
    def markIsland(self,grid,island,i,j):
        M = len(grid)
        N = len(grid[0])
        
        if i < M-1:
            if grid[i+1][j] == '1' and island[i+1][j] is False:
                island[i+1][j] = True
                self.markIsland(grid,island,i+1,j)
        if j < N-1:
            if grid[i][j+1] == '1' and island[i][j+1] is False:
                island[i][j+1] = True
                self.markIsland(grid,island,i,j+1)
        if i >= 1:
            if grid[i-1][j] == '1' and island[i-1][j] is False:
                island[i-1][j] = True
                self.markIsland(grid,island,i-1,j)
        if j >= 1:
            if grid[i][j-1] == '1' and island[i][j-1] is False:
                island[i][j-1] = True
                self.markIsland(grid,island,i,j-1)