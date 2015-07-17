"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        left_product = [0 for _ in xrange(len(nums)-1)]
        right_product = [0 for _ in xrange(len(nums)-1)]
        
        left_product[0],right_product[-1] = nums[0],nums[-1]
        for i in xrange(1,len(nums)-1):
            left_product[i] = left_product[i-1] * nums[i]
            right_product[-i-1] = right_product[-i] * nums[-i-1]
        result = [0 for _ in xrange(len(nums))]
        
        result[0] = right_product[0]
        result[-1] = left_product[-1]
        result[1:len(nums)-1] = [left_product[i-1] * right_product[i] for i in xrange(1,len(nums)-1)]
        return result