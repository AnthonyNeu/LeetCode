/*
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
*/

bool solveSudokuHelper(char** board, int boardRowSize, int boardColSize);
bool isValid(char** board, int boardRowSize, int boardColSize, int x, int y);

void solveSudoku(char** board, int boardRowSize, int boardColSize) {
    solveSudokuHelper(board, boardRowSize, boardColSize);
}

bool solveSudokuHelper(char** board, int boardRowSize, int boardColSize) {
    for (int i = 0; i < boardRowSize; i++) {
        for (int j = 0; j < boardColSize; j++) {
            if (board[i][j] != '.') continue;
            for (int c = 1; c < 10; c++) {
                board[i][j] = (char)(c + '0');
                if (isValid(board, boardRowSize, boardColSize, i, j) && solveSudokuHelper(board, boardRowSize, boardColSize)) {
                    return true;
                }
                board[i][j] = '.';
            }
            return false;
        }
    }
    return true;
}

bool isValid(char** board, int boardRowSize, int boardColSize, int x, int y) {
    /* check the row */
    for (int i = 0; i < boardRowSize; i++) {
        if (i!= y && board[x][i] == board[x][y]) return false;
    }
    /* check the col */
    for (int i = 0; i < boardColSize; i++) {
        if (i!= x && board[i][y] == board[x][y]) return false;
    }
    /* check the square */
    for (int i = 3 * (x / 3); i < 3 * (x / 3) + 3; i++) {
        for (int j = 3 * (y / 3); j < 3 * (y / 3) + 3; j++) {
            if ((x != i || y != j) && board[i][j] == board[x][y]) return false;
        }
    }
    return true;
}
