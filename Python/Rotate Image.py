"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if len(matrix)==0:
            return matrix
        
        for layer in range(len(matrix)/2):
            first = layer
            last = len(matrix) - 1 - layer
            for i in range(first,last):
                offset = i - first
                
                # save top
                top = matrix[first][i]
                
                #left -> top
                matrix[first][i] = matrix[last-offset][first]
                
                #bottom -> left
                matrix[last-offset][first] = matrix[last][last-offset]
                
                # right -> bottom
                matrix[last][last-offset] = matrix[i][last]
                
                #top -> right
                matrix[i][last] = top
                
        return matrix