"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if len(stack) == 0:
                stack.append(token)
            else:
                if token is "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif token is "-":
                    stack.append(- int(stack.pop()) + int(stack.pop()))
                elif token is "/":
                    stack.append(1/float(stack.pop()) * float(stack.pop()))
                elif token is "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    stack.append(token)
        return int(stack.pop())