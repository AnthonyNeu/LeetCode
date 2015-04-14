"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        N = len(words)
        i = 0
        result = []
        while i < N:
            j = i+1
            wordLength = len(words[i])
            while j < N and wordLength + len(words[j]) + j - i <= L:
                wordLength += len(words[j])
                j +=1
            # Last Line    
            lastLine = (j == N)
            oneWord = (j == i + 1)
            average = 1 if lastLine or oneWord else (L - wordLength)/(j-i-1)
            extra = 0 if lastLine or oneWord else (L - wordLength)%(j-i-1)
            
            s = "" + words[i]
            for k in xrange(i+1,j):
                s += ' ' * (average + 1 if extra > 0 else average)
                s += words[k]
                extra -=1
            s += (L - len(s)) * ' '
            i = j
            result.append(s)
        return result

