/*
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
*/

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        generateSubset(nums, result, new ArrayList<>(), 0);
        return result;
    }
    
    private void generateSubset(int[] nums, List<List<Integer>> result, List<Integer> cur, int step) {
        if(step == nums.length) {
            result.add(new ArrayList<>(cur));
            return;
        }
        
        generateSubset(nums, result, cur, step + 1);
        cur.add(nums[step]);
        generateSubset(nums, result, cur, step + 1);
        cur.remove(cur.size() - 1);
    }
}

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int count = (1 << nums.length) - 1;
        
        while(count >= 0){
            List<Integer> cur = new ArrayList<>();
            int idx = 0;
            while(idx < nums.length) {
                if(((count >> idx) & 1) == 1) {
                    cur.add(nums[idx]);
                }
                idx ++;
            }
            result.add(cur);
            count --;
        }
        return result;
    }
}