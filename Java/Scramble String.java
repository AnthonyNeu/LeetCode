/*
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
*/


public class Solution {
    public boolean isScramble(String s1, String s2) {
        int length = s1.length();
        if (s2.length() != length) return false;
        boolean[][][] dp = new boolean[length + 1][length][length];

        for (int i = 0 ; i < length ; i ++) {
            for (int j = 0 ; j < length ; j ++) {
                dp[1][i][j] = s1.charAt(i) == s2.charAt(j);
            }
        }
        
        for (int n = 2 ; n <= length ; n ++) {
            for (int i = 0 ; i + n <= length ; i ++) {
                for (int j = 0 ; j + n <= length ; j ++) {
                    for (int k = 1 ; k < n ; k ++) {
                        if ((dp[k][i][j] && dp[n - k][i + k][j + k]) || (dp[k][i][j + n - k] && dp[n - k][i + k][j])) {
                            dp[n][i][j] = true;
                            break;
                        }
                    }
                }
            }
        }
        
        return dp[length][0][0];
    }
}
