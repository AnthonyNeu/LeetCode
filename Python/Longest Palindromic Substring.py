"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        string = self.preProcess(s)
        palindrome = [0] * len(string) 
        center, right = 0, 0
        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]       
        
        max_len, max_center = 0, 0
        for i in xrange(1, len(string) - 1):
            if palindrome[i] > max_len:
                max_len = palindrome[i]
                max_center = i
        start = (max_center - 1 - max_len) / 2
        return s[start : start + max_len]
    
    def preProcess(self, s):
        if len(s) == 0:
            return "^$"
        string = "^"
        for i in s:
            string +=  "#" + i
        string += "#$"
        return string

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        result = s[0:1]
        
        for i in range(len(s)-1):
            p1 = self.expandAroundCenter(s,i,i)
            if len(p1) > len(result):
                result = p1
                
            p2 = self.expandAroundCenter(s,i,i+1)
            if len(p2) > len(result):
                result = p2
        return result
        
    def expandAroundCenter(self,s,c1,c2):
        l = c1
        r = c2
        M = len(s)
        while l >=0 and r < M and s[l] == s[r]:
            l -=1
            r +=1
            
        return s[l+1:r]