"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.findMinHelper(num,0,len(num)-1)
        
    def findMinHelper(self,num,left,right):
        if left >= right:
            return num[left]
        mid = left + (right - left)/2
        
        if num[mid] > num[left]:
            if num[mid] <= num[right]:#this is the normal condition
                return self.findMinHelper(num,left,mid-1)
            else:                     #don't know which part the minimum is    
                result1 = self.findMinHelper(num,mid+1,right)
                result2 = self.findMinHelper(num,left,mid-1)
                if result1 > result2:
                    return result2
                else:
                    return result1
        elif num[mid] == num[left]:   #don't know which part the minimum is  
            result1 = self.findMinHelper(num,mid+1,right)
            result2 = self.findMinHelper(num,left,mid-1)
            if result1 > result2:
                return result2
            else:
                return result1
        else:
            while mid >=1 and num[mid] >= num[mid-1]:#find the position where the array is rotated
                mid -=1
            return self.findMinHelper(num,mid,right)

class Solution:
    # @param num, a list of integer
    # @return an integer
    def bs(self, num, st, ed, res):
        if st > ed:
            return res
        else:
            mid = st + (ed - st)/2
            while num[mid]==num[ed] and mid!=ed:
                ed -= 1
            while num[mid]==num[st] and mid!=st:
                st += 1
            if num[mid] < num[ed] or mid == ed:
                res = min(res, num[mid])
                return self.bs(num, st, mid-1, res)
            else:
                res = min(res, num[st])
                return self.bs(num, mid+1, ed, res)
         
    def findMin(self, num):
        n = len(num)
        res = num[0]
        return self.bs(num, 0, n-1, res)