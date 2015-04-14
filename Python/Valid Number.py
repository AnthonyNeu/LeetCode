"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        # remove the leading and the trailing blank
        s = s.strip()
        i = 0
        
        # find whether a 'e' exists
        while i < len(s) and s[i] != 'e':
            i+=1
        if i == 0 or i == len(s) - 1:
            return False
        if i == len(s):
            return self.valid(s,False)
        return self.valid(s[:i],False) and self.valid(s[i+1:],True)
        
    def valid(self,s,hasDot):
        if len(s) == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if len(s) == 0 or s == ".":
            return False
        for i in xrange(len(s)):
            if s[i] == '.':
                if hasDot:
                    return False
                hasDot = True
                continue
            if s[i] < '0' or s[i] > '9':
                return False
        return True

class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5

# regular expression: "^\s*[\+\-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png
class Solution2:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8
        
        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE;
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char == 'E':
                inputType = InputType.EXPONENT;
                
            state = transition_table[state][inputType];
            
            if state == -1:
                return False;
        
        return state == 1 or state == 4 or state == 7 or state == 8

class Solution3:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        import re
        return bool(re.match("^\s*[\+\-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?\d+)?\s*$", s))