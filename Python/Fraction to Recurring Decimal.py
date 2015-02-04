"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
For example,
Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        result = ''
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result += '-'
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator/denominator)
        
        if numerator%denominator==0:
            return result
        else:
            result +='.'
            
        numerator %= denominator
        lookup = {}
        lookup[numerator] = len(result)
        while numerator != 0:
            numerator  = numerator*10
            result+=str(numerator/denominator)
            numerator %= denominator
            
            if lookup.has_key(numerator):
                index = lookup.get(numerator)
                result = result[:index]+'('+result[index:]
                result+=')'
                break
            lookup[numerator] = len(result)
        return result