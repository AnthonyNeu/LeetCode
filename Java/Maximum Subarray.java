/*
Find the contiguous subarray within an array (containing at least one number) that has the largest sum.
For example, given the array [2, 1, –3, 4, –1, 2, 1, –5, 4], The contiguous array [4, –1, 2, 1] has the largest sum = 6.
*/

//O(n) time and O(1) space - Dynamic Programming:
public class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 0) return 0;
        int maxEndingHere = nums[0];
        int maxSoFar = nums[0];
        for(int i = 1;i<nums.length;i++){
            maxEndingHere = Math.max(maxEndingHere+nums[i],nums[i]);
            maxSoFar = Math.max(maxSoFar,maxEndingHere);
        }
        return maxSoFar;
    }
}


//O(n log n) runtime, O(log n) stack space – Divide and Conquer:
public class Solution {
    public int maxSubArray(int[] nums) {
        return maxSubArrayHelper(nums,0,nums.length-1);
    }
    
    public int maxSubArrayHelper(int[] nums,int left,int right){
        if(left>right) return Integer.MIN_VALUE;
        int middle = left + (right - left)/2;
        int leftAnswer = maxSubArrayHelper(nums,left,middle-1);
        int rightAnswer = maxSubArrayHelper(nums,middle+1,right);
        int leftMaxSum = 0, sum = 0;
        for(int i = middle - 1;i>=left;i--){
            sum+=nums[i];
            leftMaxSum = Math.max(sum,leftMaxSum);
        }
        int rightMaxSum = 0;
        sum = 0;
        for(int i = middle + 1;i<=right;i++){
            sum+=nums[i];
            rightMaxSum = Math.max(sum,rightMaxSum);
        }
        return Math.max(leftMaxSum + nums[middle] + rightMaxSum,Math.max(leftAnswer,rightAnswer));
    }
}