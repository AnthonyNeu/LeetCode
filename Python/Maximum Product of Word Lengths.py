"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        words = sorted(words, key = lambda s : len(s))
        def bitmap(s):
            result = 0
            for c in s:
                result |= 1 << (ord(c) - ord("a"))
            return result
        bits = map(bitmap, words)
        result = 0
        i = len(words) - 1
        while i >= 0:
            # check whether each digit is 1
            if bits[i] != 67108863:
                # stop early
                if bits[i] * bits[i] <= result:
                    break
                j = i - 1
                while j >= 0:
                    candidate = len(words[i]) * len(words[j])
                    # stop early
                    if result >= candidate:
                        break
                    if bits[i] & bits[j] == 0 and candidate > result:
                        result = candidate
                    j -= 1
            i-= 1
        return result
