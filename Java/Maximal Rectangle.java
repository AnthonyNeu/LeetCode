/*
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
*/

/* Dynamic programming, O(n^3) time, O(n^2) space */
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] height = new int[m][n];
        int[][] width = new int[m][n];
        int result = 0;
        
        for (int i = 0 ; i < m ; i ++) {
            for (int j = 0 ; j < n ; j ++) {
                if (matrix[i][j] == '0') continue;
                
                width[i][j] = j == 0 ? 1 : width[i][j - 1] + 1;
                height[i][j] = i == 0 ? 1 : height[i - 1][j] + 1;
                
                int minHeight = height[i][j];
                for (int k = j ; k >= j + 1 - width[i][j] ; k --) {
                    minHeight = Math.min(minHeight, height[i][k]);
                    result = Math.max(result, minHeight * (j + 1 - k));
                }
            }
        }
        
        return result;
    }
}

/* Dynamic programming, O(n^2) time, O(n) space */
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        
        int m = matrix.length;
        int n = matrix[0].length;
        int[] height = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(right, n);
        int result = 0;
        
        for (int i = 0 ; i < m ; i ++) {
            int curLeft = 0;
            for (int j = 0 ; j < n ; j ++) {
                if (matrix[i][j] == '1') {
                    height[j] +=1;
                    left[j] = Math.max(left[j], curLeft);
                } else {
                    left[j] = 0;
                    height[j] = 0;
                    right[j] = n;
                    curLeft = j + 1;
                }
            }
            
            int curRight = n;
            for (int j = n - 1 ; j >= 0 ; j --) {
                if (matrix[i][j] == '1') {
                    right[j] = Math.min(right[j], curRight);
                    result = Math.max(result, (right[j] - left[j]) * height[j]);
                } else {
                    curRight = j;
                }
            }
        }
        
        return result;
    }
}
