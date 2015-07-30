/*
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
*/




public class Solution {
    public boolean isMatch(String s, String p) {
        int s_ptr = 0, p_ptr = 0, last_s_ptr = -1, last_p_ptr = -1;
        
        while(s_ptr < s.length()){
            if(p_ptr < p.length() && (s.charAt(s_ptr) == p.charAt(p_ptr) || p.charAt(p_ptr) == '?')){
                s_ptr += 1;
                p_ptr += 1;
            }
            else if( p_ptr < p.length() && p.charAt(p_ptr) == '*'){
                p_ptr += 1;
                last_s_ptr = s_ptr;
                last_p_ptr = p_ptr;
            }
            else if(last_p_ptr != -1){
                last_s_ptr += 1;
                s_ptr = last_s_ptr;
                p_ptr = last_p_ptr;
            }
            else{
                return false;
            }
        }
        
                    
        while (p_ptr < p.length() && p.charAt(p_ptr) == '*') p_ptr += 1;
        
        return p_ptr == p.length();
    }
}