"""
Implement int sqrt(int x).
Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        start = 0
        end = x
        
        while start < end:
            mid = (int)((start+end)/2)
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid-1
            else:
                start = mid+1
        if start * start > x:
            return start -1
        else:
            return start