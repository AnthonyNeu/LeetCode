"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

# Time O(n^3)
# Space O(n^2)
# This is a slower DP.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        M = len(matrix)
        N = len(matrix[0])
        dp = [[[0,0] for _ in xrange(N)] for _ in xrange(M)]
        
        result = 0
        
        for i in xrange(M):
            for j in xrange(N):
                if matrix[i][j] == '0':
                    continue;
                
                x = 1 if j == 0 else dp[i][j-1][0] + 1
                y = 1 if i == 0 else dp[i-1][j][1] + 1
                dp[i][j] = [x,y]
                
                minHeight = y
                for k in reversed(xrange(j-x+1,j+1)):
                    minHeight = min(minHeight,dp[i][k][1])
                    result = max(result,minHeight * (j-k+1))
        
        return result


# Time O(n^2)
# Space O(n)
# Using the result of largest rectangle area
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        M = len(matrix)
        N = len(matrix[0])
        height = [0 for _ in xrange(N)]
        result = 0
        for i in xrange(M):
            for j in xrange(N):
                height[j] = 0 if matrix[i][j] == '0' else height[j]+1
            result = max(result,self.largestRectangleArea(height))
        return result
        
    def largestRectangleArea(self, height):
        if len(height) == 0 or height is None:
            return 0
        
        res = 0
        index = [-1]
        
        for i in range(len(height)):
            while index[-1] > -1:
                if height[index[-1]] > height[i]:
                    top = index.pop()
                    res = max(res,height[top] * (i - 1 - index[-1]))
                else:
                    break
            index.append(i)
        
        while index[-1] != -1:
            top = index.pop()
            res = max(res,height[top] * (len(height) - 1 - index[-1]))
        return res

    # This is slow, as it is O(n^2),make the whole O(n^3)
    def largestRectangleArea(self, height):
        res = 0
        
        for i in reversed(xrange(len(height))):
            if i == len(height) - 1 or height[i] > height[i+1]:
                Min = 9223372036854775807
                
                for j in reversed(xrange(i+1)):
                    Min = min(Min,height[j])
                    res = max(res,(i+1-j)*Min)
        
        return res

# Time O(n^2)
# Space O(n)
# This is another faster DP.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in xrange(n)]
        H = [0 for _ in xrange(n)]
        R = [n for _ in xrange(n)]

        for i in xrange(m):
            left = 0
            for j in xrange(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1
                    
            right = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j
                    
        return result