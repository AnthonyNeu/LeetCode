/*
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
*/

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
            return searchMatrix(matrix, target, 0, 0, matrix.length - 1, matrix[0].length - 1, matrix.length - 1, matrix[0].length - 1);
        }

        private boolean searchMatrix(int[][]matrix, int target, int leftrow, int leftcol, int rightrow, int rightcol, int m, int n) {
            if(leftrow > rightrow || leftcol > rightcol || leftrow > m || rightrow > m || leftcol > n || rightcol > n) return false;

            if(target > matrix[rightrow][rightcol] || target < matrix[leftrow][leftcol]) return false;

            if(target == matrix[rightrow][rightcol] || target == matrix[leftrow][leftcol]) return true;

            int rowmid = leftrow + (rightrow - leftrow)/2;
            int colmid = leftcol + (rightcol - leftcol)/2;

            boolean flag1 = searchMatrix(matrix, target, leftrow, leftcol, rowmid, colmid, m, n);
            boolean flag2 = searchMatrix(matrix, target, leftrow, colmid + 1, rowmid, rightcol, m, n);
            boolean flag3 = searchMatrix(matrix, target, rowmid + 1, leftcol, rightrow, colmid, m, n);
            boolean flag4 = searchMatrix(matrix, target, rowmid + 1, colmid + 1, rightrow, rightcol, m, n);

            return flag1 || flag2 || flag3 || flag4;
        }
}