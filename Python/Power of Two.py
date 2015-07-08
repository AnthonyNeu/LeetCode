"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0: return False
        cur = n
        while cur != 1:
            if (cur // 2) * 2 - cur == 0:
                cur = cur/2
            else:
                return False
        return True