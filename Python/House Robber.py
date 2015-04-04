"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0 or num is None:
            return 0
            
        dp = [0 for _ in xrange(len(num) + 1)]
        
        dp[0] = 0
        dp[1] = num[0]
        
        for i in xrange(2,len(num)+1):
            dp[i] = max(dp[i-2] + num[i-1],dp[i-1])
            
        return dp[len(num)]