"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 1:
            while n % 3 == 0:
                n /= 3
        return n == 1


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log, pow
        return n > 0 and n == int(pow(3, round(log(n) / log(3))))
