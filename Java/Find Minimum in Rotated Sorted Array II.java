/*
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
*/

public class Solution {
    public int findMin(int[] nums) {
        int L = 0, R = nums.length-1;
        while(L<R && nums[L] >= nums[R]){
            int M = L + (R - L)/2;
            if(nums[M] > nums[R]) L = M+1;
            else if(nums[M] < nums[L]) R = M;
            else L = L + 1;
        }
        return nums[L];
    }
}
