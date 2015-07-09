"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones , m = 0, 1
        while m <= n:
            ones += (n/m + 8)/10 * m + (n/m %10 == 1) * (n % m + 1)
            m *= 10
        return ones