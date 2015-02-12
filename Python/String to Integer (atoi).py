"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.


Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution:
    # @return an integer
    def atoi(self, str):
        i = 0
        M = len(str)
        if M == 0:
            return 0
        sign = 1
        while i < M and str[i] is ' ':
            i+=1
        if str[i] is '-' or str[i] is '+' or str[i].isdigit() is True:
            if str[i] == '-':
                sign = -1
                i +=1
            elif str[i] == '+':
                i+=1
            tmp = ''
            while i < M and str[i].isdigit():
                tmp += str[i]
                i +=1
            N = len(tmp)
            if N == 0:
                return 0
            else:
                result = 0
                for i in range(N):
                    result = ord(tmp[i]) - ord('0') + result *10
                return max(min(result * sign, 2147483647), -2147483648)
        return 0