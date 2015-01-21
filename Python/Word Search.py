"""
Word Search:

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given
```
board = [ ["ABCE"],
          ["SFCS"],
          ["ADEE"]
          ]
```
word = "ABCCED", -> returns true,  
word = "SEE", -> returns true,  
word = "ABCB", -> returns false.
"""

"""
Time:O(M*N*4^P),Space:O(M*N+P), P is the length of string.
"""


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0] and self.isWord(board, i, j, 0, word):
                    return True
        return False
        
    # @param board, a list of lists of 1 length string
    # @param i, searching start point's row number
    # @param j, searching start point's column number
    # @param index, word[index] is the target char
    # @param word, a string
    # @return a boolean
    def isWord(self,board,i,j,index,word):
        if index == len(word):
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[index]!=board[i][j]:
            return False
            
        board[i][j] = '#'
        if self.isWord(board,i,j+1,index+1,word) or self.isWord(board,i,j-1,index+1,word) \
        or self.isWord(board,i-1,j,index+1,word) or self.isWord(board,i+1,j,index+1,word):
            return True
            
        board[i][j] = word[index]
        return False