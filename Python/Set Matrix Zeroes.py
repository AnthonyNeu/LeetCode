"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 
        
        firstrowHasZero = False
        firstcolHasZero = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstrowHasZero = True
                break
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstcolHasZero = True
                break
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstrowHasZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            
        if firstcolHasZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
