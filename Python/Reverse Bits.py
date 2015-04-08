"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in xrange(32):
            m <<=1
            m|= n & 1
            n >>=1
        return m


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        for i in xrange(32/2):
            n = self.swap(n,i,32-i-1)
        return n
            
            
    def swap(self,n,first,second):
        low = (n >> first) & 1
        high = (n >> second) & 1
        
        if low^high == 1:
            n ^= ((1 << first) | (1 << second))
        return n