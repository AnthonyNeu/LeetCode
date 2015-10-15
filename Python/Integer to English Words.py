"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
"""

class Solution(object):
    
    lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        
        result, i = '', 0
        
        while num > 0:
            if num % 1000 != 0:
                result = self.numberToWordsHelper(num % 1000) + self.thousands[i] + ' ' + result
            num /= 1000
            i += 1
        return result.rstrip()
    
    def numberToWordsHelper(self, num):
        if num == 0: return ''
        elif num < 20: return self.lessThan20[num] + ' '
        elif num < 100: return self.tens[num / 10] + ' ' + self.numberToWordsHelper(num % 10)
        else: return self.lessThan20[num / 100] + ' Hundred ' + self.numberToWordsHelper(num % 100)
