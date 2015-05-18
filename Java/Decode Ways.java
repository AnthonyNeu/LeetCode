/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
*/


public class Solution {
    public int numDecodings(String s) {
        if(s.equals("")) return 0;
        int[] way = new int[s.length()];
        for(int i=0;i<s.length();i++){
            if(i == 0 && s.charAt(0) == '0')
                return 0;
            if(s.charAt(i) - '0' >=1 && s.charAt(i) - '0' <= 26)
                way[i] = (i==0)? 1: way[i-1];
            if(i>=1){
                int twodigit = (s.charAt(i-1) - '0') * 10 + (s.charAt(i) - '0');
                if(s.charAt(i) == '0' && twodigit >26) 
                    return 0;
                if(s.charAt(i) == '0' && twodigit <= 26 && twodigit >=10)
                    way[i] = (i>=2)? way[i-2]:1;
                else if(s.charAt(i) != '0' && twodigit <= 26 && twodigit >=10)
                    way[i] = (i>=2)? way[i-2] + way[i-1]:way[i-1] + 1;
            }
        }
        return way[s.length()-1];
    }
}


public class Solution {
    public int numDecodings(String s) {
        if(s.length() == 0 || s.equals("")) return 0;
        int prev = 0, cur = 1;
        for(int i=1;i<=s.length();i++){
            if(s.charAt(i-1) == '0') cur = 0;
            
            if(i< 2 || !(s.charAt(i-2) =='1' || (s.charAt(i-2) == '2' && s.charAt(i-1) <= '6')))
                prev = 0;
            int temp = cur;
            cur = temp + prev;
            prev = temp;
        }
        return cur;
    }
}