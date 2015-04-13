"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        N = len(s1)
        dp = [[[False for _ in xrange(N)] for _ in xrange(N)] for _ in xrange(N+1)]
        
        for k in xrange(1,N+1):
            for i in xrange(N-k+1):
                for j in xrange(N-k+1):
                    if k == 1:
                        dp[k][i][j] = (s1[i] == s2[j])
                    else:
                        if dp[k][i][j] is False:
                            for p in xrange(1,k):
                                if (dp[p][i][j] and dp[k-p][i+p][j+p]) or (dp[p][i][j+k-p] and dp[k-p][i+p][j]):
                                    dp[k][i][j] = True
        return dp[N][0][0]

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True
        return self.isScrambleRe(s1, s2);
            
    def isScrambleRe(self,s1,s2):
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) == 0 or len(s1) == 1:
            return True
        for i in xrange(1,len(s1)):
            if self.isScrambleRe(s1[:i],s2[:i]) and self.isScrambleRe(s1[i:],s2[i:]) or \
            self.isScrambleRe(s1[:i],s2[-i:]) and self.isScrambleRe(s1[i:],s2[:-i]):
                return True
        return False