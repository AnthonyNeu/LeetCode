"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        num = 0
        while n > 0:
            num += n / 5
            n = n/5
        return num