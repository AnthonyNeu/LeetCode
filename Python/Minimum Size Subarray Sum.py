"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        result = 0
        p1,p2 = 0,0
        sum = 0
        while p1 < len(nums):
            while sum<s and p2 < len(nums):
                sum += nums[p2]
                p2+=1
            if sum < s:
                return result
            result = p2-p1 if result == 0 else min(p2-p1,result)
            sum = sum - nums[p1]
            p1+=1
        return result