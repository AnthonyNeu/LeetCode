/*
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
*/

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int low = searchLowBound(nums, target);
        int high = searchHighBound(nums, low, nums.length, target);
        
        int[] result;
        if(nums[low] != target){
            result = new int[] {-1, -1};
        }
        else{
            result = new int[] {low, high - 1};
        }
        
        return result;
    }
    
    private int searchLowBound(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while(low != high){
            int mid = low + (high - low) /2;
            
            if(target > nums[mid]) low = ++mid;
            else high = mid;
        }
        return low;
    }
    
    private int searchHighBound(int[] nums, int low, int high, int target) {
        while(low != high){
            int mid = low + (high - low) /2;
            
            if(target >= nums[mid]) low = ++mid;
            else high = mid;
        }
        return low;
    }
}