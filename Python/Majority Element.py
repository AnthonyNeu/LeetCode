"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 1
        candidate = num[0]
        for i in range(1,len(num)):
            if count == 0:
                candidate = num[i]
                count +=1
            elif count >= 1:
                if candidate == num[i]:
                    count +=1
                else:
                    count -=1
        return candidate