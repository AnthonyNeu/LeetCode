/*
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
*/

public class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0,right = nums.length - 1;
        while(left<=right){
            int mid = left + (right - left)/2;
            if(nums[mid] == target) return true;
            if(nums[left] < nums[mid]){
                if(nums[mid] > target && nums[left] <= target)
                    right = mid;
                else
                    left = mid + 1;
            }
            else if(nums[left] > nums[mid]){
                if(nums[mid] < target && nums[right] >= target)
                    left = mid + 1;
                else
                    right = mid;
            }
            else
                left++;
            
        }
        return false;
    }
}