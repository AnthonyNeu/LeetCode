"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""


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
            elif s[i] == ")" or s[i] == "*" or s[i] == "/":
                operators.append(s[i])
            elif s[i] == "+" or s[i] == "-":
                while operators and (operators[-1] == "*" or operators[-1] == "/"):
                    self.compute(operands,operators)
                operators.append(s[i])
            elif s[i] == "(":
                while operators[-1] != "(":
                    self.compute(operands,operators)
                operators.pop()
                
        while operators:
            self.compute(operands,operators)
            
        return operands[-1]
    
    
    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)

# use expression tree 
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops, result, number = [], [], ""
        def _calculate(left, right, op):
            i0, i1 = int(left), int(right)
            if op == "+":
                return str(i0 + i1)
            elif op == "-":
                return str(i0 - i1)
            elif op == "*":
                return str(i0 * i1)
            elif op == "/":
                return str(i0 / i1)
        for string in s:
            if string is " ":
                continue
            elif string.isdigit():
                number += string
            else:
                if number:
                    result.append(number)
                    number = ""
                if string == '-' or string == '+':
                    while ops:
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append(_calculate(left, right, op))
                    ops.append(string)
                elif string == '*' or string == '/':
                    while ops and ops[-1] not in ('+', '-'):
                        op = ops.pop()
                        right = result.pop()
                        left = result.pop()
                        result.append(_calculate(left, right, op))
                    ops.append(string)
        if number:
            result.append(number)
        while ops:
            op = ops.pop()
            right = result.pop()
            left = result.pop()
            result.append(_calculate(left, right, op))
        if not result:
            return 0
        else:
            return int(result[-1])
