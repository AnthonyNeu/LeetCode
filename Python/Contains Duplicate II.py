"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in xrange(len(nums)):
            if dic.has_key(nums[i]) and i - dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i
        return False