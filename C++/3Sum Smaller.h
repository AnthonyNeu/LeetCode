/*
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
*/

class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return 0;
        }
        sort(nums.begin(), nums.end());
        int result = 0;
        for (int i = 2; i < nums.size() ; i ++) {
            int left = 0, right = i - 1;
            while (left < right) {
                if (nums[left] + nums[right] + nums[i] < target) {
                    result += right - left;
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return result;
    }
};
