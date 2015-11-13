/*
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
*/

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        for (int i = 0 ; i < nums.size() ; i ++) {
            if (i % 2 == 1 && nums[i - 1] >= nums[i]) {
                swap(nums[i], nums[i - 1]);
            }
            else if (i != 0 && i % 2 == 0 && nums[i - 1] <= nums[i]) {
                swap(nums[i - 1], nums[i]);
            }
        }
    }
    
    void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }
};
