/*
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
*/

public class Solution {
    private String[] keyboard = new String[]{" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.length() == 0) return result;
        generateCombinations(result, 0, digits, "");
        return result;
    }
    
    private void generateCombinations(List<String> result, int cur, String digits, String path) {
        if (cur == digits.length()) {
            result.add(path);
            return;
        }
        
        for(int i = 0 ; i < keyboard[digits.charAt(cur) - '0'].length() ; i ++) {
            path += keyboard[digits.charAt(cur) - '0'].charAt(i);
            generateCombinations(result, cur + 1, digits, path);
            path = path.substring(0, path.length() - 1);
        }
    }
}
