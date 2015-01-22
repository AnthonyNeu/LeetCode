”“”
Word Break:

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
“”“
"""
This is a dynamic programming question. Every time we search for one substring of s and test whether we can find some strings in the dict to compose the substring, And for every string ,we just partition it by every single digit of the string and test whether we can get the right composition.
We create a boolean array to store the result of whether we can compose s[:i] by the string in dict. 
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        possible = []
        for i in range(len(s)):
            if s[:i + 1] in dict:
                possible.append(True)
            else:
                found = False
                for j in range(i):
                    if possible[j] == True and s[j + 1: i + 1] in dict:
                        found = True
                        break
                possible.append(found)
        return possible[len(s) - 1]