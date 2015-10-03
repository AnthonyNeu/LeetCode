/*
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
*/

public class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 0 ; i < m ; i ++) {
            for (int j = n - 1; j >= 0; j --) {
                dp[j + 1] += s.charAt(i) == t.charAt(j) ? dp[j] : 0;
            }
        }
        return dp[n];
    }
}
