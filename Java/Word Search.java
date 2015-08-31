/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
*/

public class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        for(int i = 0 ; i < m ; i ++) {
            for(int j = 0 ; j < n ; j ++) {
                if(dfs(board, visited, i , j, 0, word)) return true;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, boolean[][] visited, int i, int j, int idx, String word) {
        if(idx == word.length()) return true;
        
        if(i < 0 || j < 0 || i >= board.length || j >= board[0].length) return false;
        
        if(visited[i][j]) return false;
        
        if(board[i][j] != word.charAt(idx)) return false;
        
        visited[i][j] = true;
        boolean flag = dfs(board, visited, i - 1, j, idx + 1, word) ||
        dfs(board, visited, i, j - 1, idx + 1, word) ||
        dfs(board, visited, i, j + 1, idx + 1, word) ||
        dfs(board, visited, i + 1, j, idx + 1, word);
        visited[i][j] = false;
        return flag;
    }
}
