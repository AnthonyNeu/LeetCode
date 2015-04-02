"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ""
        
        while num > 0:
            num -=1
            
            result += chr(ord('A') + num % 26)
            num/= 26

        return result[::-1]