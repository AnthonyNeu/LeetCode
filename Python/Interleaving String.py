"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

# Time:  O(m * n)
# Space: O(m * n)
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if s1 == "":
            return s2 == s3
        elif s2 == "":
            return s1 == s3
        elif len(s1) + len(s2) != len(s3):
            return False

        dp = [[0 for _ in xrange(len(s1)+1)] for _ in xrange(len(s2)+1)]

        for i in xrange(1,len(s2)+1):
            dp[i][0] = dp[i-1][0] if s2[i-1] != s3[dp[i-1][0]] else dp[i-1][0]+1

        for i in xrange(1,len(s1)+1):
            dp[0][i] = dp[0][i-1] if s1[i-1] != s3[dp[0][i-1]] else dp[0][i-1]+1

        for i in xrange(1,len(s2)+1):
            for j in xrange(1,len(s1)+1):
                dp[i][j] = max(dp[i][j-1] + (1 if s1[j-1] == s3[dp[i][j-1]] else 0),dp[i-1][j] + (1 if s2[i-1] == s3[dp[i-1][j]] else 0))

        return dp[len(s2)][len(s1)] == len(s3)


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for i in xrange(len(s2) + 1)] for j in xrange(len(s1) + 1)]
        match[0][0] = True
        for i in xrange(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return match[-1][-1]


# Time:  O(m * n)
# Space: O(m + n)
# Dynamic Programming + Sliding Window
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            return self.isInterleave(s2, s1, s3)
        match = [False for i in xrange(len(s1) + 1)]
        match[0] = True
        for i in xrange(1, len(s1) + 1):
            match[i] = match[i -1] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in xrange(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i] and s2[j - 1] == s3[i + j - 1])
        return match[-1]