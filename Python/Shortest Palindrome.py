"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""


# this solution gets Time Limit Exceeded
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s:
            return s

        for i in reversed(xrange(1,len(s) + 1)):
            if not self.isPalindrome(s[:i]):
                continue
            else:
                return s[i:][::-1] + s

    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i].isalnum() is False:
                i += 1
            while i < j and s[j].isalnum() is False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


#KMP algorithm
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s:
            return s
            
        A = s + s[::-1]
        prefix = self.getPrefix(A)
            
        return s[prefix[-1]+1:][::-1] + s
        
    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j+1] != pattern[i]:
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix