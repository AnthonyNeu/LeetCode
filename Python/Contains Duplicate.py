"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dic = {}
        for num in nums:
            if dic.has_key(num):
                return True
            dic[num] = True
        return False