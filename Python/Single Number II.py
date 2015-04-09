"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# Time O(n)
# Space O(n)
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = {}
        for i in xrange(len(A)):
            if dic.has_key(A[i]):
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
                
        for i in xrange(len(A)):
            if dic[A[i]] < 3:
                return A[i]

# Time O(n)
# Space O(1)
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one,two,three = 0,0,0
        for number in A:
            two |= one & number
            one ^= number
            three = one & two
            one &= ~three
            two &= ~three
        return one