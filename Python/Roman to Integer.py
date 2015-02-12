"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        M = len(s)
        if M == 0:
            return 0
        i = 0
        result = 0
        while i < M:
            if s[i] == 'I':
                i +=1
                if i < M and s[i] == 'V':
                    result += 4
                elif i < M and s[i] == 'X':
                    result += 9
                elif i >= M:
                    result +=1
                    break
                else:
                    result +=1
                    i -=1
            elif s[i] == 'X':
                i +=1
                if i< M and s[i] == 'L':
                    result += 40
                elif i < M and s[i] == 'C':
                    result += 90
                elif i < 0:
                    result +=10
                    break
                else:
                    result +=10
                    i -=1
            elif s[i] == 'C':
                i +=1
                if i < M and s[i] == 'M':
                    result += 900
                elif i < M and s[i] == 'D':
                    result += 400
                elif i >= M:
                    result +=100
                    break
                else:
                    result +=100
                    i -=1
            elif s[i] == 'M':
                result += 1000
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'V':
                result += 5
            i +=1
        return result

class Solution:
    def romanToInt(self, S):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in reversed(range(len(S))):
            if i == len(S) - 1 or numeral_map[S[i]] >= numeral_map[S[i + 1]]:
                decimal += numeral_map[S[i]]
            else:
                decimal -= numeral_map[S[i]]
        return decimal