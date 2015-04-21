/*
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
*/

public class Solution {
    public String reverseWords(String s) {
        int start = 0;
        int end = s.length() - 1;
        while(start< end && s.charAt(start) == ' ') start++;
        while(start< end && s.charAt(end) == ' ' ) end--;
        StringBuilder result = new StringBuilder();
        int p1 = end + 1;
        for(int k = end;k>=start;k--)
        {
            if(s.charAt(k) == ' ')
            {
                p1 = k;
            }
            else
            {
                if(k == start || s.charAt(k-1) == ' ')
                {
                    if(result.length() != 0){
                        result.append(' ');
                    }
                    result.append(s.substring(k,p1));
                }
            }
        }
        return result.toString();
    }
}