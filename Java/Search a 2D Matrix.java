/*
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
*/

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        int low = 0;
        int high = m * n;
        
        while(low < high) {
            int mid = low + (high - low)/2;
            int value = matrix[mid/n][mid%n];
            
            if(value == target) return true;
            else if(value < target) low = mid + 1;
            else high = mid;
        }
        
        return false;
    }
}