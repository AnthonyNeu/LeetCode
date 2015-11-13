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

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return result;
        }
        int left = 0, right = matrix[0].size() - 1, top = 0, bottom = matrix.size() - 1;
        while (left <= right && top <= bottom) {
            for (int i = left ; i <= right ; i ++) {
                result.push_back(matrix[top][i]);
            }
            for (int i = top + 1 ; i < bottom ; i ++) {
                result.push_back(matrix[i][right]);
            }
            if (top < bottom) {
                for (int i = right ; i >= left ; i --) {
                    result.push_back(matrix[bottom][i]);
                }
            }
            if (left < right) {
                for (int i = bottom - 1; i > top ; i --) {
                    result.push_back(matrix[i][left]);
                }
            }
            left ++, right --, top ++, bottom --;
        }
        return result;
    }
};
