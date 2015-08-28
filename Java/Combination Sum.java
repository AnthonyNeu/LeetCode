/*
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
*/

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(result, path, candidates, 0, target);
        return result;
    }
    
    private void dfs(List<List<Integer>> result, List<Integer> path, int[] candidates, int start, int target) {
        if(target == 0) {
            result.add(new ArrayList<Integer>(path));
            return;
        }
        
        if(candidates[start] > target) return;
        
        for(int i = start ; i < candidates.length; i ++) {
            path.add(candidates[i]);
            dfs(result, path, candidates,  i, target - candidates[i]);
            path.remove(path.size() - 1);
        }
    }
}
