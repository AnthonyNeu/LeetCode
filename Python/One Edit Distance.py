"""
Given two strings S and T, determine if they are both one edit distance apart.
"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1: return False
        i, j, flag = 0, 0, False
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j] and flag:
                return False
            else:
                if len(s) == len(t):
                    flag = True
                    i += 1
                    j += 1
                elif len(s) < len(t):
                    flag = True
                    j += 1
                else:
                    flag = True
                    i += 1
        if i < len(s) or j < len(t) and flag is False:
            return True
        if i == len(s) and j == len(t) and flag:
            return True
        return False

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False
        
        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i += 1
        while i < m and s[i] == t[i + shift]:
            i += 1
            
        return i == m
