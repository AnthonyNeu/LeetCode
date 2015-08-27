/*
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
*/

public class Solution {
    private boolean[] main_diag;
    private boolean[] anti_diag;
    /*whether each column is taken*/
    private boolean[] columns;
    
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        main_diag = new boolean[2 * n];
        anti_diag = new boolean[2 * n];
        columns = new boolean[n];
        /* the column number in each row */
        int[] used = new int[n];
        
        dfs(used, result, 0);
        
        return result;
    }
    
    private void dfs(int[]used, List<List<String>> result, int row) {
        int N = used.length;
        
        if(row == N) {
            List<String> solution = new ArrayList<>();
            for(int i = 0 ; i < N ; i ++) {
                char[] charArray = new char[N];
                Arrays.fill(charArray, '.');
                String rowStr = new String(charArray);
                
                for(int j = 0 ; j < N ; j ++) {
                    if(used[i] == j) rowStr = rowStr.substring(0, j) + 'Q' + rowStr.substring(j + 1);
                }
                solution.add(rowStr);
            }
            result.add(solution);
            return;
        }
        
        /*test each columns*/
        for(int j = 0 ; j < N ; j ++) {
            boolean taken = columns[j] || main_diag[row + j] || anti_diag[row - j + N];
            if(taken) continue;
            
            used[row] = j;
            columns[j] = main_diag[row + j] = anti_diag[row - j + N] = true;
            dfs(used, result, row + 1);
            columns[j] = main_diag[row + j] = anti_diag[row - j + N] = false;
        }
    }
}
