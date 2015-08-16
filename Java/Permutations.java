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


public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        List<Integer> cur = new ArrayList<>();
        for(int i = 0 ; i < nums.length; i ++) { cur.add(nums[i]);}
        while(cur != null) {
            result.add(cur);

            cur = nextPermutation(cur);
        }

        return result;
    }

    private List<Integer> nextPermutation(List<Integer> nums) {
        List<Integer> list = new ArrayList<>(nums);
        if(list.size() == 0) return null;
        int partitionNum = list.size()-1;
        while(partitionNum>0){
            if(list.get(partitionNum - 1) < list.get(partitionNum))
                break;
            partitionNum--;
        }
        if(partitionNum == 0) return null;
        if(partitionNum > 0){
            int changeNum = list.size()-1;
            while(changeNum >= 0 && list.get(changeNum) <= list.get(partitionNum - 1)) {
                changeNum--;
            }
            int swap = list.get(changeNum);
            list.set(changeNum, nums.get(partitionNum - 1));
            list.set(partitionNum - 1, swap);
        }
        int end = list.size() - 1;
        while(end>partitionNum){
            int swap = list.get(end);
            list.set(end, list.get(partitionNum));
            list.set(partitionNum, swap);
            end--;
            partitionNum++;
        }
        return list;
    }
}
