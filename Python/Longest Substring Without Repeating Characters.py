"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
# @return an integer
    def lengthOfLongestSubstring(self, s):
        hash,i,Maxlen ={}, 0,0
        for j in range(len(s)):
            if hash.has_key(s[j]):
                Maxlen = max(Maxlen,j-i)
                while i < len(s) and s[j] != s[i]:
                    del hash[s[i]]
                    i +=1
                i+=1
            else:
                hash[s[j]] = j
        Maxlen = max(len(s)-i,Maxlen)
        return Maxlen