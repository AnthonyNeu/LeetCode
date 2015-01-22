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