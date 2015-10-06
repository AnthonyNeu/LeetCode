/*
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
*/

public class Solution {
    public int[][] generateMatrix(int n) {
        int[][] elements = new int[n][n];
        if (n == 0) return elements;
        int m = n;
        int row = 0, col = -1;
        int count = 0;
        while (true) {
            for (int i = 0; i < n; i++) {
                elements[row][++ col] = ++ count;
            }
            if (--m == 0) break;
            for (int i = 0; i < m; i++) {
                elements[++ row][col] = ++ count;
            }
            if (--n == 0) break;
            for (int i = 0; i < n; i++) {
                elements[row][-- col] = ++ count;
            }
            if (--m == 0) break;
            for (int i = 0; i < m; i++) {
                elements[-- row][col] = ++ count;
            }
            if (--n == 0) break;
        }
        return elements;
    }
}
