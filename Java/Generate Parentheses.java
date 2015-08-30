/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
*/

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> rst = new ArrayList<String>();
        if(n <= 0) {
            return rst;
        }
        getPair(rst, "", n, n);
        return rst;
    }
    
	private void getPair( List<String> rst , String s, int left, int right) {
		if(left > right || left < 0 || right < 0) {
			return; 	
		}
		if(left == 0 && right == 0) {
			rst.add(s);
			return;
		}

		getPair(rst, s + "(", left - 1, right);
		getPair(rst, s + ")", left, right - 1);
	}
}
