"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in lookup or lookup[num[i]] != num[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    