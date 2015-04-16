"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

# DP
# Time:  O(n)
# Space: O(n)
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        dp = [0 for _ in xrange(len(s) + 1)]

        for i in xrange(2,len(s) + 1):
            if s[i-1] == ')' and s[i-2] == '(':
                dp[i] = dp[i-2] + 2
            elif s[i-1] == ')' and s[i-2] == ')':
                if i - dp[i-1] - 2 >= 0 and s[i - dp[i-1] - 2] == '(':
                    dp[i] = dp[i - dp[i-1] - 2] + 2 + dp[i-1]
        return max(dp)


# Stack
# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest, last, indices = 0, -1, []
        for i in xrange(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif not indices:
                last = i
            else:
                indices.pop()
                if not indices:
                    longest = max(longest, i - last)
                else:
                    longest = max(longest, i - indices[-1])
        return longest