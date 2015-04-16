"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result, words, word_num, word_len = [], {}, len(L), len(L[0])
        for i in L:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

        for i in xrange(len(S) + 1 - word_len * word_num):
            cur, j = {}, 0
            while j < word_num:
                word = S[i + j * word_len:i + j * word_len + word_len]
                if word not in words: 
                    break
                if word not in cur: 
                    cur[word] = 1
                else:
                    cur[word] += 1
                if cur[word] > words[word]:
                    break
                j += 1
            if j == word_num:
                result.append(i)
                
        return result


# if the word is valid , but already occured maximum number of times, 
# then consider the substring starting after the first occurence of this word.set start.
class Solution:
    # @param S, a string
    # @param L, a string[]
    # @return an integer[]
    def findSubstring(self, S, L):
        result, words, word_num, word_len = [], {}, len(L), len(L[0])
        for i in L:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

        i = 0
        while i < len(S) + 1 - word_len * word_num:
            cur, j , move = {}, 0 , i
            while j < word_num:
                word = S[i + j * word_len:i + j * word_len + word_len]
                if word not in words: 
                    break
                if word not in cur: 
                    cur[word] = [i + j * word_len]
                else:
                    cur[word].append(i + j * word_len)
                if len(cur[word]) > words[word]:
                    move = cur[word][0] + word_len
                    break
                j += 1
            if j == word_num:
                result.append(i)
            if move > i:
                 i = move
            else:
                 i += 1
        return result