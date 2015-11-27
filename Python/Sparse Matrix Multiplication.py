"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return 0
        from collections import defaultdict
        m, k, n = len(A), len(A[0]), len(B[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        row = defaultdict(lambda : defaultdict(int))
        col = defaultdict(lambda : defaultdict(int))
        for i in range(m):
            for j in range(k):
                if A[i][j] is not 0:
                    row[i][j] = A[i][j]
        for j in range(n):
            for i in range(k):
                if B[i][j] is not 0:
                    col[j][i] = B[i][j]
        for i in range(m):
            for j in range(n):
                for key in row[i]:
                    if j in col and key in col[j]:
                        result[i][j] += row[i][key] * col[j][key]
        return result
