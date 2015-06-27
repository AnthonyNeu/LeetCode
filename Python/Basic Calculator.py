"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""

# My own messy code
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:return 0
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == "(":
                stack.append(s[idx])
            elif s[idx] == "-" or s[idx] == "+":
                # test calculation with multiple consecutive add or minus
                if len(stack) > 0 and isinstance(stack[-1],int):
                    symbol = stack.pop()
                    self.doCalculate(stack,symbol)
                stack.append(s[idx])
            elif s[idx] >= "0" and s[idx] <= "9":
                # build the number
                if len(stack) > 0 and isinstance(stack[-1],int):
                    num = stack.pop()
                    stack.append(int(num) * 10 + int(s[idx]))
                else:
                    stack.append(int(s[idx]))
            elif s[idx] == ")":
                temp = stack.pop()
                # test existence of calculation to de done
                if temp != "(":
                    self.doCalculate(stack,temp)
                    num = stack.pop()
                    stack.pop()
                    stack.append(num)
            idx +=1
        if len(stack) > 1:
            symbol = stack.pop()
            self.doCalculate(stack,symbol)
        return int(stack[-1])

    def doCalculate(self,stack,symbol):
        if len(stack) > 0 and (stack[-1] == "-" or stack[-1] == "+"):
            op = stack.pop()
            num = stack.pop()
            if op == "+":
                stack.append(int(num) + int(symbol))
            else:
                stack.append(int(num) - int(symbol))
        else:
            stack.append(int(symbol))

# Another version
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()
                
        while operators:
            self.compute(operands, operators)
            
        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)