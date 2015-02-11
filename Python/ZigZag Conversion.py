"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @return a string
    def convert(self, s, nRows):
        M = len(s)
        if M == 0:
            return ''
        result = []
        for i in range(nRows):
            result.append('')

        i = 0
        while i < M:
            for idx in range(nRows):
                if i < M:
                    result[idx] += s[i]
                    i +=1
            for idx in reversed(range(1,nRows-1)):
                if i < M:
                    result[idx] += s[i]
                    i +=1

        for idx in range(1,nRows):
            result[0] += result[idx]

        return result[0]