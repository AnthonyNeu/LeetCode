/*
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
*/

/* DP, O(n^2) time */
public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        int length = s.length();
        
        boolean[] dp = new boolean[length + 1];
        dp[0] = true;
        
        for (int i = 1 ; i < length + 1 ; i ++) {
            for (int j = 0 ; j < i ; j ++) {
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[length];
    }
}

/* dfs method, O(2^n) time, so cannot pass the large test case */
public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        return dfs(s, wordDict, 0, 0);
    }
    
    private boolean dfs(String s, Set<String> wordDict, int start, int cur) {
        if (cur == s.length()) {
            return wordDict.contains(s.substring(start, cur));
        }
        
        if(wordDict.contains(s.substring(start, cur))) {
            if (dfs(s, wordDict, cur + 1, cur + 1)) return true;
        }
        
        if (dfs(s, wordDict, start, cur + 1)) return true;
        
        return false;
    }
}

