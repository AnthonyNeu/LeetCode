"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        i = 0
        
        while i < N:
            if A[i] > 0 and A[i] <= N and A[A[i]-1] != A[i]:
                A[A[i]-1],A[i] = A[i],A[A[i]-1]
            else:
                i +=1
                
        for i in range(N):
            if A[i] != i+1:
                return i+1
        return N+1