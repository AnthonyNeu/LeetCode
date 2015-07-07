"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums: return nums
        prev = nums[0]
        result = [str(prev)]
        for i in xrange(1,len(nums)):
            if prev + 1 != nums[i]:
                if int(result[-1]) != prev:
                    result[-1] += "->" + str(prev)
                result.append(str(nums[i]))
            elif prev + 1 == nums[i] and i == len(nums) - 1:
                result[-1] += "->" + str(nums[i])
            prev = nums[i]
        return result