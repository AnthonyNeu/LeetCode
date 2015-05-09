/*
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
*/

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer>result = new ArrayList<>();
        if(matrix.length == 0 || matrix[0].length == 0) return result;
        int left = 0,right = matrix[0].length-1,top = 0,bottom = matrix.length-1;
        while(left <= right && top <= bottom){
            for(int i=left;i<right+1;i++)
                result.add(matrix[top][i]);
            for(int i=top+1;i<bottom;i++)
                result.add(matrix[i][right]);
            for(int i=right;i>=left;i--){
                if(top<bottom)
                    result.add(matrix[bottom][i]);
            }
            for(int i=bottom-1;i>=top+1;i--){
                if(left<right)
                    result.add(matrix[i][left]);
            }
            left++;right--;top++;bottom--;
        }
        return result;
    }
}

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> elements = new ArrayList<>();
        if (matrix.length == 0) return elements;
        int m = matrix.length, n = matrix[0].length;
        int row = 0, col = -1;
        while (true) {
            for (int i = 0; i < n; i++) {
                elements.add(matrix[row][++col]);
            }
            if (--m == 0) break;
            for (int i = 0; i < m; i++) {
                elements.add(matrix[++row][col]);
            }
            if (--n == 0) break;
            for (int i = 0; i < n; i++) {
                elements.add(matrix[row][--col]);
            }
            if (--m == 0) break;
            for (int i = 0; i < m; i++) {
                elements.add(matrix[--row][col]);
            }
            if (--n == 0) break;
        }
        return elements;
    }
}