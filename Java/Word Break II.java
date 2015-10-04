/*
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
*/

public class Solution {
    public List<String> wordBreak(String s, Set<String> wordDict) {
        int length = s.length();
        
        boolean[] dp = new boolean[length + 1];
        dp[0] = true;
        boolean[][] table = new boolean[length + 1][length];
        
        for (int i = 1 ; i < length + 1 ; i ++) {
            for (int j = 0 ; j < i ; j ++) {
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    table[i][j] = true;
                }
            }
        }
        
        List<String> result = new ArrayList<>();
        List<String> path = new ArrayList<>();
        getPath(s, table, result, path, s.length());
        return result;
    }
    
    private void getPath(String s, boolean[][] table, List<String> result, List<String> path, int cur) {
        if (cur == 0) {
            StringBuilder sb = new StringBuilder();
            for (int i = path.size() - 1 ; i >= 0 ; i --) {
                sb.append(path.get(i)).append(" ");
            }
            result.add(sb.toString().substring(0, sb.length() - 1));
        }
        
        for (int i = 0 ; i < s.length(); i ++) {
            if (table[cur][i]) {
                path.add(s.substring(i, cur));
                getPath(s, table, result, path, i);
                path.remove(path.size() - 1);
            }
        }
    }
}

