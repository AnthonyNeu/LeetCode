"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        table = {}
        for i in xrange(len(s)):
            if s[i] not in table:
                table[s[i]] = 1
            else:
                table[s[i]] += 1
        
        for i in xrange(len(t)):
            if t[i] in table and table[t[i]] > 0:
                table[t[i]] -= 1
            else:
                return False
        return True
