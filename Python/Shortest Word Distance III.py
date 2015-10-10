"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        table = {}
        for i, word in enumerate(words):
            if word in table:
                table[word].append(i)
            else:
                table[word] = [i]
            
        min_length = float('inf')
        if word1 != word2:
            for i in xrange(len(table[word1])):
                for j in xrange(len(table[word2])):
                    min_length = min(min_length, abs(table[word1][i] - table[word2][j]))
        else:
            for i in xrange(len(table[word1]) - 1):
                min_length = min(min_length, table[word1][i + 1] - table[word1][i])
        return min_length

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                if index1 is not None:
                    dist = min(dist, i - index1)
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1

        return dist
