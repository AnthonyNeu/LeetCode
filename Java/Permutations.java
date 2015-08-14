/*
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
*/

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        Arrays.fill(used, false);
        generatePermutation(nums, cur, result, used, nums.length);
        
        return result;
    }
    
    private void generatePermutation(int[]nums, List<Integer> cur, List<List<Integer>> result, boolean[] used, int remain) {
        if(remain == 0) {
            result.add(new ArrayList<>(cur));
        }
        
        for(int i = 0 ; i < nums.length ; i ++) {
            if(used[i] == true) continue;
            used[i] = true;
            cur.add(nums[i]);
            generatePermutation(nums, cur, result, used, remain - 1);
            used[i] = false;
            cur.remove(cur.size() - 1);
        }
    }
}
