"""
Implement pow(x, n).
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return self.pow(1/x,-n)
        elif n == 0:
            return 1
        else:
            if n % 2 == 0:
                temp = self.pow(x,n/2)
                return temp*temp
            else:
                temp = self.pow(x,n//2)
                return temp*temp*x