"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
class Solution:
    def wordBreak(self, s, dict):
        n = len(s)
        f = [False for _ in xrange(n)]
        trace = [[False] * n for _ in xrange(n)]
        for i in xrange(n):
            if s[:i+1] in dict:
                f[i] = True
                trace[0][i] = True
            for j in xrange(i):
                if f[j] and s[j+1:i+1] in dict:
                    f[i] = True
                    trace[j+1][i] = True
        result = []
        if f[n-1]:
            self.backtrack(s, trace, 0, [], result)
        return result
    
    def backtrack(self, s, trace, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return
        for i in xrange(start, len(s)):
            if trace[start][i]:
                self.backtrack(s, trace, i + 1, path + [s[start:i+1]], result)

class Solution:  
    """ The alternative solution is to precheck before actually break the words.
    """
    def canBreak(self, s, dict):
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
        
    def wordBreak(self, s, dict):
        result = {}
        if not self.canBreak(s, dict):
            return []
        for i in range(len(s)):
            result[s[:i + 1]] = []
            if s[:i + 1] in dict:
                result[s[:i + 1]] = [s[:i + 1]]
            for j in range(i):
                if s[:j + 1] in result and s[j + 1: i + 1] in dict:
                    for k in result[s[:j + 1]]:
                        result[s[:i + 1]].append(k + " " + s[j + 1: i + 1])
        return result[s]

# this solution use the previous checking pass's result
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        result = {}
        self.max_length, n = float('inf'), len(s)
        self.possible = [False] * (n + 1)
        
        def canBreak():
            if len(wordDict) == 0:
                return len(s) == 0
            self.possible[0] = True
            self.max_length = max([len(w) for w in wordDict])
            for i in range(1, n + 1):
                for j in range(1, min(i, self.max_length) + 1):
                    if not self.possible[i - j]:
                        continue
                    if s[i - j:i] in wordDict:
                        self.possible[i] = True
                        break
            return self.possible[n]
        if not canBreak():
            return []
        for i in range(1, n + 1):
            result[s[:i]] = []
            for j in range(1, min(i, self.max_length) + 1):
                if not self.possible[i - j]:
                    continue
                if s[i - j:i] in wordDict:
                    if i == j:
                        result[s[:i]].append(s[:i])
                    else:
                        for candidate in result[s[:i - j]]:
                            result[s[:i]].append(candidate + " " + s[i - j:i])
        return result[s[:n]]
