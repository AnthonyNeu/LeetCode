/*
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
*/

public class Solution {
    private boolean[] main_diag;
    private boolean[] anti_diag;
    /*whether each column is taken*/
    private boolean[] columns;
    private int result = 0;
    
    public int totalNQueens(int n) {
        main_diag = new boolean[2 * n];
        anti_diag = new boolean[2 * n];
        columns = new boolean[n];
        /* the column number in each row */
        int[] used = new int[n];
        
        dfs(used, 0);
        
        return result;
    }
    
    private void dfs(int[]used, int row) {
        int N = used.length;
        
        if(row == N) {
            result ++;
            return;
        }
        
        /*test each columns*/
        for(int j = 0 ; j < N ; j ++) {
            boolean taken = columns[j] || main_diag[row + j] || anti_diag[row - j + N];
            if(taken) continue;
            
            used[row] = j;
            columns[j] = main_diag[row + j] = anti_diag[row - j + N] = true;
            dfs(used, row + 1);
            columns[j] = main_diag[row + j] = anti_diag[row - j + N] = false;
        }
    }
}
