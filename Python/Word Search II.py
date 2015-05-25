"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. 
What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? 
If you would like to learn how to implement a basic trie, 
please work on this problem: Implement Trie (Prefix Tree) first.
"""


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.flag = False
        self.children = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        result = {}
        trie = TrieNode()
        for word in words:
            trie.insert(word)
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.findWordsRecu(board,trie,result,visited,[],i,j)
                
        return result.keys()
            
    def findWordsRecu(self,board,trie,result,visited,current,i,j):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return 
        
        if board[i][j] not in trie.children:
            return 
        
        current.append(board[i][j])
        nextNode = trie.children[board[i][j]]
        if nextNode.flag:
            result["".join(current)] = True
            
        visited[i][j] = True
        self.findWordsRecu(board,nextNode,result,visited,current,i+1,j)
        self.findWordsRecu(board,nextNode,result,visited,current,i,j+1)
        self.findWordsRecu(board,nextNode,result,visited,current,i,j-1)
        self.findWordsRecu(board,nextNode,result,visited,current,i-1,j)
        visited[i][j] = False
        current.pop()