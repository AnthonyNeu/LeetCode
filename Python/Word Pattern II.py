"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, 0, 0, {})
        
    def dfs(self, pattern, str, pattern_next, str_start, dic):
        if pattern_next == len(pattern) and str_start == len(str):
            return len(dic) == len(set(dic.values()))
        elif pattern_next == len(pattern) or str_start == len(str):
            return False
        
        char = pattern[pattern_next]
        for i in range(str_start + 1, len(str) + 1):
            if len(str) - i + 1 < len(pattern) - pattern_next:
                break
            cur = str[str_start:i]
            if char not in dic:
                dic[char] = cur
                if self.dfs(pattern, str, pattern_next + 1, i, dic):
                    return True
                del dic[char]
            else:
                if dic[char] == cur and self.dfs(pattern, str, pattern_next + 1, i, dic):
                    return True
        return False
        