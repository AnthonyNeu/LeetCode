"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if A is None:
            return False
        return self.searchHelper(A,0,len(A)-1,target)
        
    def searchHelper(self,a,left,right,x):
        mid = (left + right)/2
        if a[mid] == x:
            return True
        if right < left:
            return False
        
        """
        Either the left or right half must be normally ordered
        Find out which part is normally ordered, and then figure out 
        which part to search.
        """
        if a[left] < a[mid]:#Left is normally ordered
            if x >=a[left] and x <=a[mid]:
                return self.searchHelper(a,left,mid-1,x)
            else:
                return self.searchHelper(a,mid+1,right,x)
        elif a[mid] < a[left]:#Right is normally ordered
            if x >=a[mid] and x <=a[right]:
                return self.searchHelper(a,mid+1,right,x)
            else:
                return self.searchHelper(a,left,mid-1,x)
        elif a[left] == a[mid]:#Left half is all repeated
            if a[mid] != a[right]:#if right is diff,search it
                return self.searchHelper(a,mid+1,right,x)
            else:#else, we need to seach both halves
                result = self.searchHelper(a,left,mid-1,x)
                if result == False:
                    return self.searchHelper(a,mid+1,right,x)
                else:
                    return result
        return False