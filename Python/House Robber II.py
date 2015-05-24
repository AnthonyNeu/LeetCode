"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 1: return nums[0]
        return max(self.robHelper(nums[0:len(nums)-1]),self.robHelper(nums[1:]))
    
    def robHelper(self, num):
        if len(num) == 0 or num is None:
            return 0
            
        dp = [0 for _ in xrange(len(num) + 1)]
        
        dp[0] = 0
        dp[1] = num[0]
        
        for i in xrange(2,len(num)+1):
            dp[i] = max(dp[i-2] + num[i-1],dp[i-1])
            
        return dp[len(num)]