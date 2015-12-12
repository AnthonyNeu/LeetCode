"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""

# https://leetcode.com/discuss/73761/a-short-o-n-recursive-greedy-solution
# prove that the greedy solution get the optimal solution by exchange the solution to the optimal one
# O(26 * n) time, n is the length of string
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0 for _ in range(26)]
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        pos = 0
        for i in range(len(s)):
            if ord(s[pos]) > ord(s[i]):
                pos = i
            count[ord(s[i]) - ord('a')] -= 1
            if count[ord(s[i]) - ord('a')] == 0:
                break
        return "" if len(s) == 0 else s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))

# using stack
# https://leetcode.com/discuss/73824/short-16ms-solution-using-stack-which-can-optimized-down-4ms
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = [0 for _ in range(26)]
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
        visited = [False] * 26
        result = []
        for c in s:
            counter[ord(c) - ord('a')] -= 1
            if visited[ord(c) - ord('a')] or (result and result[-1] == c):
                continue
            # search for a better solution with less lexicographical rank
            # check whether the last element in the stack can be remove or not
            while result and result[-1] > c and counter[ord(result[-1]) - ord('a')] > 0:
                visited[ord(result[-1]) - ord('a')] = False
                result.pop()
            result.append(c)
            visited[ord(c) - ord('a')] = True
        return ''.join(result)
