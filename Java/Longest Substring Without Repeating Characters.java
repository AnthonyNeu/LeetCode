/*
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
*/

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int [] table = new int[256];
        Arrays.fill(table,-1);
        int start = 0;
        int result = 0;
        for(int j = 0;j<s.length();j++)
        {
            if(table[s.charAt(j)] >= start)
            {
                start = table[s.charAt(j)] + 1;
            }
            table[s.charAt(j)] = j;
            result = Math.max(result,j - start +1);
        }
        return result;
    }
}