/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return;
        }
        int n = matrix.size();
        for (int layer = 0 ; layer < n / 2 ; layer ++) {
            int first = layer, last = n - first - 1;
            for (int i = first ; i < last ; i ++) {
                int top = matrix[first][i];
                int offset = i - first;
                matrix[first][i] = matrix[last - offset][first];
                matrix[last - offset][first] = matrix[last][last - offset];
                matrix[last][last - offset] = matrix[i][last];
                matrix[i][last] = top;
            }
        }
    }
};

// rotate upside down and then rotate the upside part to downside part
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        reverse(matrix.begin(), matrix.end());
        for (int i = 0; i < matrix.size() ; ++i) {
            for (int j = 0 ; j < i ; ++j)
                swap(matrix[i][j], matrix[j][i]);
        }
    }
};
