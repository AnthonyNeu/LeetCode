"""
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
Note:
Your solution should be in logarithmic complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if num is None:
            return None
        return self.findPeakHelper(num,0,len(num)-1)
        
    def findPeakHelper(self,num,start,end):
        if start == end:
            return start
        elif start + 1 == end:
            if num[start] > num[end]:
                return start
            else:
                return end
        else:
            mid = (start + end)/2
            if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
                return mid
            elif num[mid] < num[mid-1] and num[mid] > num[mid+1]:
                return self.findPeakHelper(num,start,mid-1)
            else:
                return self.findPeakHelper(num,mid+1,end)