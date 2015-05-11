/*
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
*/

public class Solution {
    private Map<Character, Integer> map =
      new HashMap<Character, Integer>() {{
            put('I', 1);  put('V', 5);   put('X', 10);
            put('L', 50); put('C', 100); put('D', 500);
            put('M', 1000);
    }};
    
    public int romanToInt(String s) {
        int prev = 0, total = 0;
        for(char c:s.toCharArray()){
            int curr = map.get(c);
            total += (curr > prev) ? curr - 2 * prev:curr;
            prev = curr;
        }
        return total;
    }
}