/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
*/

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right && nums[left] >= nums[right]) {
            int mid = left + (right - left) / 2;
            if (nums[left] <= nums[mid]) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return nums[left] > nums[right] ? nums[right] : nums[left];
    }
};
