"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        result = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix[0])):
            result[0][i] = int(matrix[0][i])
            
        for i in xrange(len(matrix)):
            result[i][0] = int(matrix[i][0])
        
        Max = 1 if (sum(result[0][:]) != 0 or sum(result[:][0]) != 0) else 0
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix[0])):
                if matrix[i][j] == "1" and matrix[i-1][j] == "1" and matrix[i][j-1] == "1" and matrix[i-1][j-1] == "1":
                    a = int(result[i-1][j-1] ** (1/2.0))
                    
                    #test the zero in the horizontal line and vertical line
                    hasZero = False
                    #if has zero, calculate the min squre based on (i,j)
                    Min = float('inf')
                    for m in xrange(i-a,i-1):
                        if matrix[m][j] == "0":
                            hasZero = True
                            Min = i - m
                    for m in xrange(j-a,j-1):
                        if matrix[i][m] == "0":
                            hasZero = True
                            Min = min(Min,j-m)
                    result[i][j] = (a+1) ** 2 if hasZero == False else Min ** 2
                else:
                    result[i][j] = int(matrix[i][j])
                Max = max(Max,result[i][j])
        return Max
                    
                    
                    
                    