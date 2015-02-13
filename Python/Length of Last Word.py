"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == ' ':
            return 0
        i = 0
        j = len(s)-1
        while j >=0 and s[j] == ' ':
            j-=1
            i+=1
        # all is ' '
        if j < 0:
            return 0
        while j >= 0 and s[j] != ' ':
            j-=1
        return len(s)-1 - j - i

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
