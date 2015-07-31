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



public class Solution {
    private enum InputType{
        INVALID,SPACE,SIGN,DIGIT,DOT,EXPONENT,NUM_INPUT;

        public static int convert(InputType type){
            switch (type){
                case INVALID:
                    return 0;
                case SPACE:
                    return 1;
                case SIGN:
                    return 2;
                case DIGIT:
                    return 3;
                case DOT:
                    return 4;
                case EXPONENT:
                    return 5;
                case NUM_INPUT:
                    return 6;
                default:
                    break;
            }
            return -1;
        }
    }

    private int transistionTable[][] = new int[][]{
            {-1,  0,  3,  1,  2, -1},
            {-1,  8, -1,  1,  4,  5},
            {-1, -1, -1,  4, -1, -1},
            {-1, -1, -1,  1,  2, -1},
            {-1,  8, -1,  4, -1,  5},
            {-1, -1,  6,  7, -1, -1},
            {-1, -1, -1,  7, -1, -1},
            {-1,  8, -1,  7, -1, -1},
            {-1,  8, -1, -1, -1, -1}
    };

    public boolean isNumber(String s) {
        int state = 0 ;
        for(int i = 0 ; i < s.length() ; i ++){
            InputType type = InputType.INVALID;
            if(s.charAt(i) == ' '){
                type = InputType.SPACE;
            }
            else if(s.charAt(i) == '+' || s.charAt(i) == '-'){
                type = InputType.SIGN;
            }
            else if(Character.isDigit(s.charAt(i))){
                type = InputType.DIGIT;
            }
            else if(s.charAt(i) == '.'){
                type = InputType.DOT;
            }
            else if(s.charAt(i)== 'e'){
                type = InputType.EXPONENT;
            }

            state = transistionTable[state][InputType.convert(type)];

            if(state == -1) return false;
        }

        return state == 1 || state == 4 || state == 7 || state == 8;
    }
}