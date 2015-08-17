/*
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
*/

public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> rst = new ArrayList<>();
        List<Integer> solution = new ArrayList<>();
        
        helper(rst, solution, n, k, 1);
        return rst;
    }
    
    private void helper(
        List<List<Integer>> rst, 
        List<Integer> solution, 
        int n, 
        int k, 
        int start) {

        if (solution.size() == k){
            rst.add(new ArrayList(solution));
            return;
        }
        
        for(int i = start; i<= n; i++){
            solution.add(i);
            
            // the new start should be after the next number after i
            helper(rst, solution, n, k, i+1); 
            solution.remove(solution.size() - 1);
        }
    }
}
