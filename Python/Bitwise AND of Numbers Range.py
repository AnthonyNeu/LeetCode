"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        N = n - m
        if N == 0:
            return m
        result  = 0
        k = 0
        while N / (2** k) != 0:
            k +=1
        result |= (m>>k)<<k
        result &= (n>>k)<<k
        return result