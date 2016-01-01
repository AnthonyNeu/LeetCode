"""
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result, n = [], len(word)

        def helper(cur, start):
            if start == n:
                result.append(''.join(cur))
                return
            helper(cur + [word[start]], start + 1)
            candidate = []
            if cur and cur[-1].isdigit():
                candidate = list(cur)
                candidate[-1] = str(int(cur[-1]) + 1)
            else:
                candidate = cur + ['1']
            helper(candidate, start + 1)
        helper([], 0)
        return result

# A more cleaner version.
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result, n = [], len(word)

        def helper(cur, start, count):
            if start == n:
                if count > 0:
                    cur += str(count)
                result.append(cur)
                return
            helper(cur + (str(count) if count > 0 else "") + word[start], start + 1, 0)
            helper(cur, start + 1, count + 1)
        helper("", 0, 0)
        return result

# Bit Manipulation
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        """
        As each position can be whether the original character or 1, so there are 2^n result.
        We use the same method in Subset to emumerate all the possbile solution.
        """
        result, n = [], len(word)

        def helper(mask):
            candidate, count = "", 0
            for i in range(n):
                if mask % 2 == 1:
                    count += 1
                else:
                    if count > 0:
                        candidate += str(count)
                    candidate += word[i]
                    count = 0
                mask >>= 1
            if count:
                candidate += str(count)
            return candidate
        for i in range(1 << n):
            result.append(helper(i))
        return result
