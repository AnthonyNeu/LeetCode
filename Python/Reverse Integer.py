"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        ans = 0
        if x >= 0:
            while x:
                ans = ans * 10 + x % 10
                x /= 10
            if ans > 2147483647:
                return 0
            return ans
        else:
            if ans < - 2147483648:
                return 0
            return -self.reverse(-x)