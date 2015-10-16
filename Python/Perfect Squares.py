"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

class Solution1(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

# from https://leetcode.com/problems/perfect-squares/
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = [i*i for i in range(1, int(n**0.5)+1)]
        visited = [False] * (n+1)
        level = 0
        children = [0]
        while True:
            level += 1
            parents = children
            children = []
            for parent in parents:
                for edge in edges:
                    child = parent + edge
                    if child == n:
                        return level
                    if child > n:
                        break
                    if visited[child]:
                        continue
                    visited[child] = True
                    children.append(child)
                    