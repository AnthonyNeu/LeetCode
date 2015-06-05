/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/


public class Solution {
    public void rotate(int[][] matrix) {
        if(matrix.length == 0) return;
        
        for(int layer = 0;layer < matrix.length/2;layer++){
            int first = layer;
            int last = matrix.length - 1 - first;
            for(int i = first;i<last;i++){
                int offset = i - layer;
                int top = matrix[first][i];
                
                matrix[first][i] = matrix[last - offset][first];
                
                matrix[last - offset][first] = matrix[last][last - offset];
                
                matrix[last][last - offset] = matrix[i][last];
                
                matrix[i][last] = top;
            }
        }
    }
}


public class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        for(int i = 0; i<n;i++)
            for(int j = 0;j<n-i;j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][n-1-i];
                matrix[n-1-j][n-1-i] = temp;
            }
                
        for(int i = 0;i<n/2;i++)
            for(int j = 0;j<n;j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-i][j];
                matrix[n-1-i][j] = temp;
            }
    }
}