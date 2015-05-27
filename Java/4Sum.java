/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
*/


//O(n^4) time,O(1) space
public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        for (int i = 0; i < nums.length-3; i++) 
            for(int j = i+1; j < nums.length-2;j++){
                if((i == 0 || nums[i]!=nums[i-1]) && (j == i+1 || nums[j]!= nums[j-1])){
                    int low = j + 1, high = nums.length - 1, sum = target - nums[i] - nums[j];
                    while(low<high){
                        if(nums[low] + nums[high] == sum){ 
                            res.add(Arrays.asList(nums[i],nums[j],nums[low],nums[high]));
                            while(low<high && nums[low] == nums[low+1]) low++;
                            while(low<high && nums[high] == nums[high-1]) high--;
                            low++;high--;
                        }   
                        else if(nums[low] + nums[high] < sum) low++;
                        else high--;
                    }
            }
        }
        return res;
    }
}

//O(n^2) time,O(n^4) worst case, O(n^2) space 
public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        //create a hashmap to store sums of two elements
        Map<Integer, ArrayList<ArrayList<Integer>>> map = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int sum = nums[i] + nums[j];
                ArrayList<Integer> pair = new ArrayList<Integer>(2);
                pair.add(i);
                pair.add(j);
                if (!map.containsKey(sum)) {
                    ArrayList<ArrayList<Integer>> sumpair = new ArrayList<>();
                    sumpair.add(pair);
                    map.put(sum, sumpair);
                } else {
                    ArrayList<ArrayList<Integer>> sumpair = map.get(sum);
                    sumpair.add(pair);
                }
            }
        }
         
        //use hashset to remove duplicates
        HashSet<List<Integer>> set = new HashSet<>();
        List<List<Integer>> ret = new LinkedList<>();
        for (Integer sum : map.keySet()) {
            ArrayList<ArrayList<Integer>> sumpair = map.get(sum);
            if (map.containsKey(target - sum)) {
                if (target - sum == sum && sumpair.size() == 1)
                    continue;
                ArrayList<ArrayList<Integer>> pairs = map.get(target - sum);
                for (ArrayList<Integer> pair1 : sumpair) {
                    for (ArrayList<Integer> pair2 : pairs) {
                        //check if the two pairs have the same element
                        if (pair1.contains(pair2.get(0)) || pair1.contains(pair2.get(1)))
                            continue;
                        List<Integer> list = new LinkedList<>();
                        list.add(nums[pair1.get(0)]);
                        list.add(nums[pair1.get(1)]);
                        list.add(nums[pair2.get(0)]);
                        list.add(nums[pair2.get(1)]);
                        Collections.sort(list);
                        set.add(list);
                    }
                }
            }
        }
        ret.addAll(set);
        return ret;
    }
}