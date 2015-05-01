"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dic1 = {}
        dic2 = {}
        match1 = [0 for _ in xrange(len(s))]
        match2 = [0 for _ in xrange(len(t))]
        if(len(s) != len(t)):
            return False
        for i in xrange(len(s)):
            if dic1.has_key(s[i]):
                match1[i] = dic1[s[i]]
            else:
                match1[i] = i
            dic1[s[i]] = i
            if dic2.has_key(t[i]):
                match2[i] = dic2[t[i]]
            else:
                match2[i] = i
            dic2[t[i]] = i
        for i in xrange(len(s)):
            if match1[i] != match2[i]:
                return False
        return True


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        return dict(zip(s, t)) == dict(reversed(zip(s, t))) and dict(zip(t, s)) == dict(reversed(zip(t, s)))

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
    
        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        res = {}
        for i in xrange(len(s)):
            if s[i] not in res:
                res[s[i]] = t[i]
            elif res[s[i]] != t[i]:
                return False
        return True