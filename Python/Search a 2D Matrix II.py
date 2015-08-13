"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        N = len(matrix[0])
        return self.searchMatrixHelper(matrix,target,0,0,N-1,M-1)

    def searchMatrixHelper(self,matrix,target,l,u,r,d):
        if l > r or u > d:
            return False
        if target < matrix[u][l] or target > matrix[d][r]:
            return False
        mid = l + (r - l)/2
        row = u
        
        while row <= d and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1;
        return self.searchMatrixHelper(matrix,target,mid+1,u,r,row-1) or self.searchMatrixHelper(matrix,target,l,row,mid-1,d)