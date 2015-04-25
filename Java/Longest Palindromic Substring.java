/*
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
*/

//O(n^2) time,O(1) space
public class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 0)
            return "";
        String result = s.substring(0,1);
        for(int i = 0; i<s.length() - 1;i++)
        {
            String p1 = expandAroundCenter(s,i,i);
            if(result.length() < p1.length())
                result = p1;
            String p2 = expandAroundCenter(s,i,i+1);
            if(result.length() < p2.length())
                result = p2;
        }
        return result;
    }
    
    private String expandAroundCenter(String s,int c1, int c2)
    {
        int left = c1,right = c2;
        while (left >=0 && right<= s.length() - 1 && s.charAt(left) == s.charAt(right))
        {
            left--;
            right++;
        }
        return s.substring(left+1,right);
    }
}