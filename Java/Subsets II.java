/*
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
*/

public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        generateSubset(nums, result, new ArrayList<>(), 0);
        return result;
    }
    
    private void generateSubset(int[] nums, List<List<Integer>> result, List<Integer> cur, int step) {
        result.add(new ArrayList<>(cur));
        
        for(int i = step ; i < nums.length ; i ++) {
            if(i != step && nums[i-1] == nums[i]) continue;
            cur.add(nums[i]);
            generateSubset(nums, result, cur, i + 1);
            cur.remove(cur.size() - 1);
        }
    }
}

public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
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
            if(!result.contains(cur)) {
                result.add(cur);
            }
            count --;
        }
        return result;
    }
}
