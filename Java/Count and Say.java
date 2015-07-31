/*
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
*/


public class Solution {
    public String countAndSay(int n) {
        String s = "1";
        
        while(--n > 0){
            s = getNext(s);
        }
        
        return s;
    }
    
    private String getNext(String s){
        StringBuilder sb = new StringBuilder();
        
        int idx = 0;
        while(idx < s.length()){
            int count = 1;
            while(idx < s.length() - 1 && s.charAt(idx) == s.charAt(idx+1)){
                idx ++;
                count ++;
            }
            
            sb.append(count).append(s.charAt(idx));
            idx ++;
        }
        
        return sb.toString();
    }
}