"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start, end, range = 0, len(A) - 1, []
        previousIndex = self.findPreviousIndex(A,start,end,target)
        nextIndex = self.findNextIndex(A,start,end,target)
        if previousIndex + 1 == nextIndex:
            return [-1,-1]
        else:
            return [previousIndex + 1 , nextIndex - 1]
        
    def findPreviousIndex(self,A,start,end,target):
        if start > end:
            return end
        mid = (start + end)/2
        if A[mid] < target:
            return self.findPreviousIndex(A,mid+1,end,target)
        else:
            return self.findPreviousIndex(A,start,mid-1,target)
     
    def findNextIndex(self,A,start,end,target):
        if start > end:
            return start
        mid = (start + end)/2
        if A[mid] <= target:
            return self.findNextIndex(A,mid+1,end,target)
        else:
            return self.findNextIndex(A,start,mid-1,target)  