/*
A robot is located at the top-left corner of a m × n grid (marked ‘Start’ in the diagram below). 
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below). 
How many possible unique paths are there?
*/

//O(mn)runtime, O(mn)space – Bottom-up dynamic programming:
public class Solution {
    public int uniquePaths(int m, int n) {
        if(m == 0 || n == 0) return 0;
        int[][] mat = new int[m][n];
        for(int i = 0 ; i< m ; i++)
            for(int j = 0; j < n; j++){
                if(i == 0 || j == 0) mat[i][j] = 1;
                else
                    mat[i][j] = mat[i][j-1] + mat[i-1][j];
            }
        return mat[m-1][n-1];
    }
}

//O(mn)runtime, O(n)space – Bottom-up dynamic programming:
public class Solution {
    public int uniquePaths(int m, int n) {
        if(m == 0 || n == 0) return 0;
        int[] f = new int[n];
        f[0] = 1;
        for(int i = 0 ; i< m ; i++)
            for(int j = 1; j < n; j++){
                f[j] = f[j] + f[j - 1];
            }
        return f[n-1];
    }
}
