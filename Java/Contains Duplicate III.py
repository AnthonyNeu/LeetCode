"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n//t
            for m in (dic.get(key-1),dic.get(key),dic.get(key+1)):
                if m is not None and abs(n-m) <=t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False