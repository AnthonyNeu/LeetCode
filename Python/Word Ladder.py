"""
Word Ladder:

Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
"""
Solution:Bread-first seach for all possible trace of transformation.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = collections.deque([start])
        length = 1
        while len(queue)>0:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == end:
                    return length
                N = len(word)
                for j in range(N):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        condidate = word[:j] + char + word[j+1:]
                        if condidate in dict:
                            queue.append(condidate)
                            dict.remove(condidate)
            length += 1
        return 0

# 2 BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        words1 = set([beginWord])
        words2 = set([endWord])
        # if beginWord in wordList:
        #     wordList.remove(beginWord)
        # if endWord in wordList:
        #     wordList.remove(endWord)

        def find_ladder(words1, words2, level):
            if len(words1) == 0:
                return 0
            if len(words1) > len(words2):
                return find_ladder(words2, words1, level)
            words3 = set()
            for word in words1:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            candidate = word[:i] + j + word[i + 1:]
                            if candidate in words2:
                                return level + 1
                            if candidate in wordList:
                                words3.add(candidate)
                                wordList.remove(candidate)
            return find_ladder(words3, words2, level+1)
        return find_ladder(words1, words2, 1)
