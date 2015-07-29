/*
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
*/

public class Solution {
    public boolean isMatch(String s, String p) {
        if(p.length() == 0) return s.length() == 0;

        //next is not '*', then must match this one
        if(p.length() > 1 && p.charAt(1) != '*' || p.length() == 1){
            if( s.length() != 0 && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.')){
                return p.length() >= 1 && s.length() >= 1 && isMatch(s.substring(1),p.substring(1));
            }
            else{
                return false;
            }
        }
        //next is '*'
        else 
        {
            int idx = 0;
            while( s.substring(idx).length() != 0 && (s.charAt(idx) == p.charAt(0) || p.charAt(0) == '.') ){
                if(isMatch(s.substring(idx),p.substring(2))){
                    return true;
                }
                idx ++;
            }
            return isMatch(s.substring(idx),p.substring(2));
        }
    }
}
