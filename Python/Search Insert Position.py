"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low, high = 0, len(A)
        
        while low < high:
            mid = low + (high - low) / 2
            
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                if mid < len(A) -1 and A[mid+1] >target:
                    return mid+1
                low = mid +1
            else:
                if mid > 0 and A[mid-1] <target:
                    return mid
                high = mid -1
                    
        return low