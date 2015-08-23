/*
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
*/

public class Solution {
    public void solve(char[][] board) {
        if(board.length == 0 || board[0].length == 0) return;
        
        int m = board.length;
        int n = board[0].length;
        for(int i = 0 ; i < m ; i ++) {
            for(int j = 0 ; j < n ; j ++) {
                if(i == 0 || i == m - 1 || j == 0 || j == n - 1) bfs(board, i, j);
            }
        }
        
        for(int i = 0 ; i < m ; i ++) {
            for(int j = 0 ; j < n ; j ++) {
                if(board[i][j] == 'V') board[i][j] = 'O';
                else if(board[i][j] == 'O') board[i][j] = 'X';
            }
        }
    }
    
    private void bfs(char[][]board, int row, int col) {
        if(board[row][col] != 'O') return;
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(Arrays.asList(row, col));
        
        while(!queue.isEmpty()) {
            List<Integer> list = queue.poll();
            int i = list.get(0);
            int j = list.get(1);
            if(i < 0 || i >= board.length || j < 0 || j >= board[0].length) continue;
            if(board[i][j] != 'O') continue;
            board[i][j] = 'V';
            queue.offer(Arrays.asList(i + 1, j));
            queue.offer(Arrays.asList(i - 1, j));
            queue.offer(Arrays.asList(i, j + 1));
            queue.offer(Arrays.asList(i, j - 1));
        }
    }
}
