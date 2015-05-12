/*
You are climbing a staircase. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?
*/


public class Solution {
    public int climbStairs(int n) {
        int prev = 1, curr = 1;
        for(int i = 1; i < n ;i++){
            int temp = curr;
            curr += prev;
            prev = temp;
        }
        return curr;
    }
}