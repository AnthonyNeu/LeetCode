/*
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
*/

public class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0 ; i < m + 1 ; i ++) {
            dp[i][0] = i;
        }
        
        for (int i = 0 ; i < n + 1 ; i ++) {
            dp[0][i] = i;
        }
        
        for (int i = 1 ; i < m + 1 ; i ++) {
            for (int j = 1 ; j < n + 1 ; j ++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i - 1][j]) + 1;
                    dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + 1);
                }
            }
        }
        return dp[m][n];
    }
}
