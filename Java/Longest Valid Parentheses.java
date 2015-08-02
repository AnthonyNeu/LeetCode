/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
*/

//Using stack, O(n) time and O(n) space
public class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        int max_len = 0 , last_idx = -1;
        
        for(int i = 0 ; i < s.length() ; i ++){
            if(s.charAt(i) == '('){
                stack.push(i);
            }
            else{
                if(stack.empty()){
                    last_idx = i;
                }                
                else{
                    stack.pop();
                    if(stack.empty()){
                        max_len = Math.max(max_len, i - last_idx);
                    }
                    else{
                        max_len = Math.max(max_len, i - stack.peek());
                    }
                }
            }
        }
        
        return max_len;
    }
}

//two passes, O(n) time and O(1) space
public class Solution {
    public int longestValidParentheses(String s) {
        int result = 0, bound = 0, score = 0, start = 0, cur = 0;
        
        while(cur < s.length()){
            score += s.charAt(cur) == '(' ? 1 : -1;
            
            if(score == 0){
                result = Math.max(result, cur - start + 1);
            }
            else if(score < 0){
                start = cur + 1;
                score = 0;
            }
            cur ++;
        }
        
        if (score > 0) {
            bound = start - 1;
            cur = s.length() - 1;
            start = cur;
            score = 0;

            while (cur > bound) {
                score += (s.charAt(cur) == ')') ? 1 : -1;

                if (score == 0) {
                    result = Math.max(result, start - cur + 1);             
                } else if (score < 0) {
                    start = cur - 1;
                    score = 0;
                }

                --cur;
            }
        }
        
        return result;
    }
}

//two passes, O(n) time and O(1) space
public class Solution {
    public int longestValidParentheses(String s) {
        int result = 0, depth = 0, start = -1;
        
        for(int i = 0 ; i < s.length() ; i ++){
            if(s.charAt(i) == '('){
                depth ++;
            }
            else{
                depth --;
                if(depth == 0){
                    result = Math.max(result, i - start);
                }
                else if(depth < 0){
                    start = i;
                    depth = 0;
                }
            }
        }
        
        depth = 0;
        start = s.length();
        for(int i = s.length() - 1 ; i >= 0 ; i --){
            if(s.charAt(i) == ')'){
                depth ++;
            }
            else{
                depth --;
                if(depth == 0){
                    result = Math.max(result, start - i);
                }
                else if(depth < 0){
                    start = i;
                    depth = 0;
                }
            }
        }
        
        return result;
    }
}