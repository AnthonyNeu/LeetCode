"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        lookup = {}
        result = []
        for s in strs:
            tmp = ''.join(sorted(s))
            lookup.setdefault(tmp,[]).append(s)
        for key in lookup:
            if len(lookup[key])>1:
                result.extend(lookup[key])
        return result