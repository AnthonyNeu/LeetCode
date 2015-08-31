/*
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
*/

public class Solution {
    public void solveSudoku(char[][] board) {
        solveSudokuHelper(board);
    }
    
    private boolean solveSudokuHelper(char[][] board) {
        for(int i = 0 ; i < 9 ; i ++) {
            for(int j = 0 ; j < 9 ; j ++) {
                if(board[i][j] == '.') {
                    for(int m = 1 ; m < 10 ; m ++) {
                        board[i][j] = (char)(m + '0');
                        if(isValid(board, i, j) && solveSudokuHelper(board)) return true;
                        board[i][j] = '.';
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, int x, int y) {
        /* check the row */
        for(int i = 0 ; i < 9 ; i ++) {
            if(i != y && board[x][i] == board[x][y]) return false;
        }
        
        /* check the column */
        for(int i = 0 ; i < 9 ; i ++) {
            if(i != x && board[i][y] == board[x][y]) return false;
        }
        
        /* check the squre */
        for(int i = 3 * (x / 3) ; i < 3 * (x / 3) + 3 ; i ++) {
            for(int j = 3 * (y / 3) ; j < 3 * (y / 3) + 3 ; j ++) {
                if((i != x || j != y) && board[i][j] == board[x][y]) return false;
            }
        }
        return true;
    }
}
