"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSum = A[0]
        maxEnd = A[0]
        for i in range(1,len(A)):
            maxEnd = max(maxEnd+A[i],A[i])
            maxSum = max(maxSum,maxEnd)
        return maxSum


# Greedy Algorithm
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        Max = A[0]
        current = 0
        
        for num in A:
            current += num
            Max = max(Max,current)
            current = max(0,current)
        return Max