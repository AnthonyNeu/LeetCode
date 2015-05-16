"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class WordDictionary:
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchRecu(0,word,self.root)
        
    def searchRecu(self,start,word,cur):
        if start == len(word):
            return cur.flag
        if word[start] in cur.children:
            return self.searchRecu(start+1,word,cur.children[word[start]])
        elif word[start] == '.':
            for c in cur.children:
                if self.searchRecu(start+1,word,cur.children[c]):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")