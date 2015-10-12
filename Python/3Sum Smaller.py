"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(len(nums)):
            x = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < x:
                    result += right - left
                    left += 1
                elif nums[left] + nums[right] >= x:
                    right -= 1
        return result
