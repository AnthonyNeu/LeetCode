"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) is 0:
            return True
        
        length = len(A)
        idx = 0
        while idx < length -1:
            if A[idx] == 0:
                flag = False
                for i in range(idx):
                    if A[i] + i > idx:
                        flag = True
                if flag == False:
                    return False
                else:
                    start = idx
            idx = idx + 1
        return True

class Solution:
    # @param nums, an integer[]
    # @return a boolean
    def canJump(self, nums):
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last:
                # if not last one and can't go further
                if (curr == last) and (last < len(nums)-1):
                    return False   # never reach the last one
                last = curr
            curr = max(curr, i+nums[i])
        return True
