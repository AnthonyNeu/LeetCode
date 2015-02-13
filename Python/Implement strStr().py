"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) ==0:
            return 0
        value = hash(needle)
        for i in range(len(haystack) - len(needle)+1):
            if hash(haystack[i:i+len(needle)]) == value:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1