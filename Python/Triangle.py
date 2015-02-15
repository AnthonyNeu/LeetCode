"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        d = [[0 for _ in range(len(triangle[j]))] for j in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0 and j == 0:
                    d[0][0] = triangle[0][0]
                elif j == 0:
                    d[i][0]  = triangle[i][0] + d[i-1][0]
                elif j == len(triangle[i]) - 1:
                    d[i][j]  = triangle[i][j] + d[i-1][j-1]
                else:
                    d[i][j]  = min(d[i-1][j-1],d[i-1][j]) + triangle[i][j]
        result = sorted(d[len(triangle)-1])
        return result[0]

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        N = len(triangle)
        d = triangle[len(triangle)-1]
        for i in reversed(range(N-1)):
            for j in range(i+1):
                d[j] = min(d[j],d[j+1]) + triangle[i][j]
                
        return d[0]
