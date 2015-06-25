"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

# DP
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
                    

# DP with sliding window.
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(2)]
        max_size = 0
        
        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])
            
        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i % 2][0] = 1
            else:
                size[i % 2][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[i % 2][j - 1], \
                                         size[(i - 1) % 2][j], \
                                         size[(i - 1) % 2][j - 1]) + 1
                    max_size = max(max_size, size[i % 2][j])
                else:
                    size[i % 2][j] = 0
                    
        return max_size * max_size


# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution2:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(m)]
        max_size = 0
        
        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])
            
        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            else:
                size[i][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i][j - 1],  \
                                     size[i - 1][j],  \
                                     size[i - 1][j - 1]) + 1
                    max_size = max(max_size, size[i][j])
                else:
                    size[i][j] = 0
                    
        return max_size * max_size
        
        
# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution3:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        H, W = 0, 1
        # DP table stores (h, w) for each (i, j).
        table = [[[0, 0] for j in xrange(len(matrix[0]))] \
                         for i in xrange(len(matrix))]
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                # Find the largest h such that (i, j) to (i + h - 1, j) are feasible.
                # Find the largest w such that (i, j) to (i, j + w - 1) are feasible.
                if matrix[i][j] == '1':
                    h, w = 1, 1
                    if i + 1 < len(matrix):
                        h = table[i + 1][j][H] + 1
                    if j + 1 < len(matrix[i]):
                        w = table[i][j + 1][W] + 1
                    table[i][j] = [h, w]
        
        # A table stores the length of largest square for each (i, j).
        s = [[0 for j in xrange(len(matrix[0]))] \
                for i in xrange(len(matrix))]
        max_square_area = 0
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                side = min(table[i][j][H], table[i][j][W])
                if matrix[i][j] == '1':
                    # Get the length of largest square with bottom-left corner (i, j).
                    if i + 1 < len(matrix) and j + 1 < len(matrix[i + 1]):
                        side = min(s[i + 1][j + 1] + 1, side)
                    s[i][j] = side
                    max_square_area = max(max_square_area, side * side)
                    
        return max_square_area;       
                    
                    