"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == [] or matrix[0] == []:
            return result
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return result