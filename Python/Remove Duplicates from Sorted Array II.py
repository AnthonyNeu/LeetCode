"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 1
        idx = 1
        state = 0
        while i < len(A):
            if A[i] != A[i-1]:
                state = 0
                A[idx] = A[i]
                idx +=1
            elif A[i] == A[i-1]:
                # first time
                if state == 0:
                    A[idx] = A[i]
                    idx +=1
                    state = 1
            i +=1    
        return min(len(A),idx)