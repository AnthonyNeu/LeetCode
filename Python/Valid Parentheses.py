"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        M = len(s)
        while M > 0:
            if len(stack) == 0:
                stack.append(s[len(s)-M])
                M-=1
            else:
                c = stack.pop()
                tmp = s[len(s) - M]
                if c is '(' and tmp is ')' or c is '[' and tmp is ']' or c is '{' and tmp is '}':
                    M-=1
                else:
                    stack.append(c)
                    stack.append(s[len(s)-M])
                    M -=1
        if len(stack) == 0:
            return True
        else:
            return False