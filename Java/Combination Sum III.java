/*
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
*/

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        dfs(result, 1, n, list, k);
        return result;
    }
 
    public void dfs(List<List<Integer>> result, int start, int sum, List<Integer> list, int k){
        if(sum==0 && list.size()==k){
            result.add(new ArrayList<Integer>(list));
        }
     
        for(int i=start; i<=9; i++){
            if(sum-i<0) break;
            if(list.size()>k) break;
     
            list.add(i);
            dfs(result, i+1, sum-i, list, k);
            list.remove(list.size()-1);
        }
    }
}
