"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

# Dynamic Programming
# Time O(m*n)
# Space O(m*n)
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return False
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]
                    
        return result[len(s)][len(p)]

	def isMatch(self, s, p):
	    l = len(s)
	    if len(p) - p.count('*') > l:
	        return False
	    dp = [True]  + [False] * l
	    for letter in p:
	        new_dp = [dp[0] and letter == '*']
	        if letter == '*':
	            for j in range(l):
	                new_dp.append(new_dp[-1] or dp[j + 1])
	        elif letter == '?':
	            new_dp += dp[:l]
	        else:
	            new_dp += [dp[j] and s[j] == letter for j in range(l)]
	        dp = new_dp
	    return dp[-1]

# iteration
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_p_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                return False
            
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        return p_ptr == len(p)

# recursive, slowest
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s
        
        if p[0] != '*':
            if not s or (p[0] == s[0] or p[0] == '?'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0:
                if self.isMatch(s, p[1:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[1:])