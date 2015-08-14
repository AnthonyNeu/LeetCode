/*
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
*/

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        Arrays.sort(nums);
        Arrays.fill(used, false);
        generatePermutation(nums, cur, result, used, nums.length);
        
        return result;
    }
    
    private void generatePermutation(int[]nums, List<Integer> cur, List<List<Integer>> result, boolean[] used, int remain) {
        if(remain == 0) {
            result.add(new ArrayList<>(cur));
        }
        
        Integer prev = null;
        for(int i = 0 ; i < nums.length ; i ++) {
            if(used[i] == true) continue;
            if(prev!= null && nums[i] == prev) continue;
            used[i] = true;
            cur.add(nums[i]);
            generatePermutation(nums, cur, result, used, remain - 1);
            used[i] = false;
            cur.remove(cur.size() - 1);
            prev = nums[i];
        }
    }
}