/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
*/

/*dfs O(2^n) time and O(n) space*/
public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> path = new ArrayList<>();

        dfs(s, result, path, 0, 1);
        return result;
    }

    private void dfs(String s, List<List<String>> result, List<String> path, int prev, int start) {
        if(start == s.length()) {
            /*test whether s[prev:start-1] is palindrome*/
            /*if it is true, then must add it to one result*/
            if(isPalindrome(s, prev, start - 1)) {
                path.add(s.substring(prev, start));
                result.add(new ArrayList<>(path));
                path.remove(path.size() - 1);
            }
            return;
        }

        /*do dfs, search for the next palindrome*/
        dfs(s, result, path, prev, start + 1);
        if(isPalindrome(s, prev, start - 1)) {
            path.add(s.substring(prev, start));
            dfs(s, result, path, start, start + 1);
            path.remove(path.size() - 1);
        }
    }
    
    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if(s.charAt(start)!=s.charAt(end)) return false;
            start ++;
            end --;
        }
        return true;
    }
}

/*dfs O(2^n) time and O(n) space*/
public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> path = new ArrayList<>();

        dfs(s, result, path, 0);
        return result;
    }

    private void dfs(String s, List<List<String>> result, List<String> path, int start) {
        if(start == s.length()) {
            result.add(new ArrayList<>(path));
            return;
        }

        for(int i = start ; i < s.length() ; i ++ ) {
            if(isPalindrome(s, start, i)) {
                path.add(s.substring(start, i + 1));
                dfs(s, result, path, i + 1);
                path.remove(path.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if(s.charAt(start)!=s.charAt(end)) return false;
            start ++;
            end --;
        }
        return true;
    }
}

/*dp O(2^n) time and O(1) space*/
public class Solution {
    public List<List<String>> partition(String s) {
        int n = s.length();
        boolean[][] lookup = new boolean[n][n];

        for(int i = n - 1 ; i >= 0 ; i --) {
            for(int j = i ; j < n ; j ++) {
                lookup[i][j] = s.charAt(i) == s.charAt(j) && ( (j - i < 2) || (lookup[i + 1][j - 1] == true));
            }
        }

        List<List<List<String>>> result = new ArrayList<>();
        for(int i = 0 ; i < n ; i ++) {
            result.add(new ArrayList<>());
        }
        
        for(int i = n - 1 ; i >= 0 ; i --) {
            for(int j = i ; j < n ; j ++) {
                if(lookup[i][j]) {
                    String palindrome = s.substring(i , j + 1);
                    /* if this is not the last palindrome */
                    if(j + 1 < n) {
                        for(List<String> list : result.get(j + 1)) {
                            Collections.reverse(list);
                            list.add(palindrome);
                            Collections.reverse(list);
                            result.get(i).add(new ArrayList<String>(list));
                            list.remove(0);
                        }
                    }
                    else {
                        result.get(i).add(new ArrayList<String>(Arrays.asList(palindrome)));
                    }
                }
            }
        }
        return result.get(0);
    }
}
