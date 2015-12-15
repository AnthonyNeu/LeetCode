"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        M = len(num1)
        N = len(num2)
        
        if M == 0 or N == 0:
            return '0'
        
        result = [0 for i in range(M+N+1)]
        
        for i in range(M):
            carry = 0
            n1 = ord(num1[M - i - 1]) - ord('0')
            for j in range(N):
                n2 = ord(num2[N - j - 1]) - ord('0')
                sum = n1 * n2 + result[i + j] + carry
                carry = sum/10
                result[i+j] = sum%10
            if carry > 0:
                result[i+N] +=carry
        
        start = M + N
        while start>=0 and result[start] == 0:
            start -=1
        # if we get two  0 * 0
        if start == -1:
            return '0'
        s = ''
        for i in reversed(range(0,start+1)):
            s += chr(result[i] + ord('0'))
        return s

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                result[i + j] += int(e1) * int(e2)
                result[i + j + 1] += result[i + j] / 10
                result[i + j] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return "".join(map(str, result[::-1]))
