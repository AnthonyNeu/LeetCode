"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True
        for i in xrange(1, len(p)+1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]
        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if result[i][j] is True:
                    continue
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    result[i][j] = result[i-1][j-1]
                elif p[j-1] == '*' and (p[j-2] == s[i-1] or p[j-2] == '.'):
                	# if we want to let the * to represent a zero preceding element
                    result[i][j] = result[i][j-1] or result[i][j-2]
                    k = i + 1
                    while k <= len(s) and (p[j-2] == '.' or p[j-2] == s[k-1]):
                            result[k][j] = result[k-1][j]
                            k +=1
                elif p[j-1] == '*' and p[j-2] != s[i-1]:
                    if j >=2:
                        result[i][j] = result[i][j-2]
        return result[len(s)][len(p)]

# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        
        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]
                    
        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i][j] = result[i][j-2] or (result[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                    
        return result[len(s)][len(p)]