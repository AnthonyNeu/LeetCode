"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        nums = [lower - 1] + nums + [upper + 1]
        
        for i, num in enumerate(nums[:-1]):
            if nums[i + 1] - num <= 1: continue
            else: result.append(self.buildRange(num + 1, nums[i + 1] - 1))
        
        return result
            
        
    def buildRange(self, lower, upper):
        if lower == upper:
            return str(lower)
        else:
            s = str(lower) + "->" + str(upper)
            return s
