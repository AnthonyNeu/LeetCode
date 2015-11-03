"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

# O(nlogn)
class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        
        def insert(target):
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if dp[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(dp):
                if left == 0 or dp[-1] != target:
                    dp.append(target)
            else:
                dp[left] = target
        for num in nums:
            insert(num)
        return len(dp)

# O(n^2)
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if nums is not None and len(nums) > 0 else 0
