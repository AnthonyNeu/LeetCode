/*
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
*/

public class Solution {
    private static final Set<String> OPERATORS = new HashSet<>(Arrays.asList("+", "-", "*", "/"));
    
    private int eval(int x,int y,String op){
        switch(op){
            case "+" : return x + y;
            case "-" : return x - y;
            case "*" : return x * y;
            default: return x / y;
            }
    } 
    
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String token :tokens){
            if(OPERATORS.contains(token)){
                int y = stack.pop();
                int x = stack.pop();
                stack.push(eval(x,y,token));
            }
            else{
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
}


//A cleaner way use interface
public class Solution {
    interface Operator {
        int eval(int x, int y);
    }
    
    private static final Map<String, Operator> OPERATORS =
        new HashMap<String, Operator>() {{
            put("+", new Operator() {
               public int eval(int x, int y) { return x + y; }
            });
            put("-", new Operator() {
               public int eval(int x, int y) { return x - y; }
            });
            put("*", new Operator() {
               public int eval(int x, int y) { return x * y; }
            });
            put("/", new Operator() {
               public int eval(int x, int y) { return x / y; }
            });
    }};

    public int evalRPN(String[] tokens) {
       Stack<Integer> stack = new Stack<>();
       for (String token : tokens) {
          if (OPERATORS.containsKey(token)) {
             int y = stack.pop();
             int x = stack.pop();
             stack.push(OPERATORS.get(token).eval(x, y));
          } else {
             stack.push(Integer.parseInt(token));
          } 
       }
       return stack.pop();
    }
}