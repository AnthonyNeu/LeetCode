"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37
"""

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        list1 = version1.split('.')
        list2 = version2.split('.')
        i = min(len(list1),len(list2))
        j = 0
        while j < i:
            if int(list1[j]) < int(list2[j]):
                return -1
            elif int(list1[j]) > int(list2[j]):
                return 1
            else:
                j +=1
        
        if i < len(list1):
            tmp = ''.join(list1[len(list2):])
            for char in '123456789':
                if char in tmp:
                    return 1
            else:
                return 0
        elif i < len(list2):
            tmp = ''.join(list2[len(list1):])
            for char in '123456789':
                if char in tmp:
                    return -1
            else:
                return 0
        elif i == len(list1) and i == len(list2):
            return 0

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1, v2 = version1.split("."), version2.split(".")
        
        if len(v1) > len(v2):
            v2 += ['0' for _ in xrange(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in xrange(len(v2) - len(v1))]
        
        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1
        
        return 0