/*
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
*/

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return 0;
        }
        int result = 0, m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> height(m, vector<int>(n, 0));
        vector<vector<int>> width(m, vector<int>(n, 0));
        for (int i = 0 ; i < m ; i ++) {
            for (int j = 0 ; j < n ; j ++) {
                if (matrix[i][j] == '0') continue;
                width[i][j] = j == 0 ? 1 : width[i][j - 1] + 1;
                height[i][j] = i == 0 ? 1 : height[i - 1][j] + 1;
                int minHeight = height[i][j];
                for (int k = j ; k >= j + 1 - width[i][j] ; k --) {
                    minHeight = min(minHeight, height[i][k]);
                    result = max(result, minHeight * (j - k + 1));
                }
            }
        }
        return result;
    }
};

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return 0;
        }
        const int m = matrix.size();
        const int n = matrix.front().size();
        int result = 0;
        vector<int> height(n, 0);  // height of all ones rectangle include matrix[i][j]
        vector<int> left(n, 0);  // left closed bound of all ones rectangle include matrix[i][j]
        vector<int> right(n, n);  // right open bound of all onces rectangle include matrix[i][j]
        for (int i = 0 ; i < m ; i ++) {
            int curLeft = 0;
            for (int j = 0 ; j < n ; j ++) {
                if (matrix[i][j] == '1') {
                    height[j] += 1;
                    left[j] = max(left[j], curLeft);
                } else {
                    right[j] = n, left[j] = 0, height[j] = 0;
                    curLeft = j + 1;
                }
            }
            int curRight = n;
            for (int j = n - 1 ; j >= 0 ; j --) {
                if (matrix[i][j] == '1') {
                    right[j] = min(right[j], curRight);
                    result = max(result, (right[j] - left[j]) * height[j]);
                } else {
                    curRight = j;
                }
            }
        }
        return result;
    }
};
