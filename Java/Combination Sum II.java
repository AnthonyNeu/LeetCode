/*
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
*/

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if(candidates.length == 0) return result;
        
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
        
        int prev = -1;
        for(int i = start; i < candidates.length; i ++) {
            if(candidates[start] > target) return;
            if(i > start && prev == candidates[i]) continue;
            path.add(candidates[i]);
            dfs(result, path, candidates,  i + 1, target - candidates[i]);
            path.remove(path.size() - 1);
            prev = candidates[i];
        }
    }
}
