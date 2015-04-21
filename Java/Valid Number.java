/*
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
*/

public class Solution {
    public boolean isNumber(String s) {
        s = s.trim();
        
        //find the 'e'
        int i = 0;
        while (i<s.length() && s.charAt(i) != 'e')
            i++;
        if(i == 0 || i == s.length()-1)
            return false;
        if(i == s.length())
            return valid(s,false);
        return valid(s.substring(0,i),false) && valid(s.substring(i+1,s.length()),true);
    }
    
    private boolean valid(String s,boolean hasdot)
    {
        if(s.length() == 0)
            return false;
        if(s.charAt(0) == '+' || s.charAt(0) == '-')
            s = s.substring(1,s.length());
        if(s.length() == 0 || s.equals("."))
            return false;
        for(int i = 0;i<s.length();i++)
        {
            if(s.charAt(i) == '.')
            {
                if(hasdot)
                    return false;
                hasdot = true;
            }
            else if(s.charAt(i) < '0' || s.charAt(i) > '9')
                return false;
        }
        return true;
    }
}