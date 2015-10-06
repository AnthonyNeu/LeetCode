/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
*/

public class Solution {
    public String minWindow(String s, String t) {
        int[] expect = new int[256];
        int[] current = new int[256];
        
        for (char c : t.toCharArray()) {
            expect[c] ++;
        }
        
        int i = 0, minWidth = Integer.MAX_VALUE, minStart = 0, count = 0, start = 0;
        
        while (i < s.length()) {
            current[s.charAt(i)] ++;
            
            if (current[s.charAt(i)] <= expect[s.charAt(i)]) count ++;
            
            if (count == t.length()) {
                while (expect[s.charAt(start)] == 0 || expect[s.charAt(start)]  < current[s.charAt(start)]) {
                    current[s.charAt(start)] --;
                    start ++;
                }
                
                if (minWidth > i - start + 1) {
                    minWidth = i - start + 1;
                    minStart = start;
                }
            }
            
            i ++;
        }
        
        if (minWidth == Integer.MAX_VALUE) return "";
        
        return s.substring(minStart, minStart + minWidth);
    }
}
