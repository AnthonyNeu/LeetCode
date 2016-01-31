/*
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

// O(n) time and O(n) space
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int len = nums.size();
        vector<int> result;
        unordered_map<int, int> lookup;
        for (int i = 0; i < len; ++i) {
            int numberToFind = target - nums[i];
            if (lookup.find(numberToFind) != lookup.end()) {
                result.push_back(lookup[numberToFind] + 1);
                result.push_back(i + 1);
                return result;
            }
            lookup[nums[i]] = i;
        }
    }
};

// O(n log n) time and O(n) space
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        int start = 0, end = sorted.size() - 1;

        while (start < end) {
            if (sorted[start] + sorted[end] > target) end--;
            else if (sorted[start] + sorted[end] < target) start++;
            else break;
        }

        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == sorted[start]) ans.push_back(i + 1);
            else if (nums[i] == sorted[end]) ans.push_back(i + 1);
        }
        if (ans[0]>ans[1])
            swap(ans[0], ans[1]);
        return ans;
    }
};
