"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        
        i = len(digits)-1
        carry = 0
        while i >= 0:
            if i == len(digits)-1:
                temp = digits[i] + 1
                carry = temp/10
                digits[i] = temp%10
            else:
                temp = digits[i] + carry
                carry = temp/10
                digits[i] = temp%10
            
            if carry == 0:
                return digits

            i -=1
        if carry >0:
            digits.insert(0,carry)
        return digits