/*
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
*/

public class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length();
        int n = num2.length();
        
        if (m == 0 || n == 0) return "0";
        
        int[] result = new int[n + m + 1];
        for (int i = 0 ; i < m ; i ++) {
            int carry = 0;
            int n1 = num1.charAt(m - 1 - i) - '0';
            for (int j = 0 ; j < n ; j ++) {
                int n2 = num2.charAt(n - 1 - j) - '0';
                int sum = n1 * n2 + result[i + j] + carry;
                carry = sum / 10;
                result[i + j] = sum % 10;
            }
            
            if (carry > 0) {
                result[i + n] = result[i + n] + carry;
            }
        }
        
        int start = m + n;
        while (start >= 0 && result[start] == 0) {
            start --;
        }
        
        if (start == -1) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (int i = start ; i >= 0 ; i --) {
            sb.append(result[i]);
        }
        
        return sb.toString();
    }
}
