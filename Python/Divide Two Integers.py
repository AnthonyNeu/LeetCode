"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            if result > 2147483648:
                result = 2147483648
            return -result
        else:
            if result > 2147483647:
                result = 2147483647
            return result