/*
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
*/


public class Solution {
    public int maxProduct(int[] nums) {
        if(nums.length == 0) return 0;
        int result = nums[0], max = nums[0], min = nums[0];
        for(int i = 1;i < nums.length;i++){
            int mn = min,mx = max;
            max = Math.max(nums[i],Math.max(mx*nums[i],mn*nums[i]));
            min = Math.min(nums[i],Math.min(mx*nums[i],mn*nums[i]));
            result = Math.max(result,max);
        }
        return result;
    }
}