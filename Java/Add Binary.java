/*
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
*/

public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int length = a.length() > b.length() ? a.length() : b.length();
        int carry = 0;
        for(int i = 0 ; i < length ; i ++){
            int ai = i < a.length() ? a.charAt(a.length() - 1 - i) - '0' : 0;
            int bi = i < b.length() ? b.charAt(b.length() - 1 - i) - '0' : 0;
            int val = (ai + bi + carry) % 2;
            carry = (ai + bi + carry) / 2;
            sb.append(val);
        }
        if(carry > 0){
            sb.append(carry);
        }
        
        return sb.reverse().toString();
    }
}