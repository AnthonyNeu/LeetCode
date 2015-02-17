"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 1
        idx = 1
        while i < len(A):
            if A[i] != A[i-1]:
                A[idx] = A[i]
                idx +=1
            i +=1    
        return min(len(A),idx)