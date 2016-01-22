"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if memo[x][y] == 0:
                for i in range(4):
                    nx, ny = x + directions[i][0], y + directions[i][1]
                    if 0 <= nx < m and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
                        memo[x][y] = max(memo[x][y], dfs(nx, ny))
                memo[x][y] += 1
            return memo[x][y]
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result
