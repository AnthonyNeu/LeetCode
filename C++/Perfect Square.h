/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
*/

class Solution1 {
public:
    int numSquares(int n) {
        static vector<int> num{0};
        while (num.size() <= n) {
            int squares = numeric_limits<int>::max();
            for (int i = 1; i * i <= num.size(); ++i) {
                squares = min(squares, num[num.size() - i * i] + 1);
            }
            num.emplace_back(squares);
        }
        return num[n];
    }
};

class Solution2 {
public:
    int numSquares(int n) {
        int numberOfEdge = int(sqrt(n)) + 1;
        vector<int> edges(numberOfEdge);
        for (int i = 0 ; i < numberOfEdge ; i ++) {
            edges[i] = i * i;
        }
        vector<bool> visited(n + 1, false);
        vector<int> children{0};
        int level = 0;
        while (true) {
            level ++;
            vector<int> parents(children);
            children.clear();
            for (int parent : parents) {
                for (int edge : edges) {
                    int child = parent + edge;
                    if (child == n) {
                        return level;
                    } else if (child > n) {
                        break;
                    } 
                    if (visited[child]) {
                        continue;
                    }
                    visited[child] = true;
                    children.emplace_back(child);
                }
            }
        }
    }
};
