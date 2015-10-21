"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

# O(nlogn) time
class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low < high:
            mid = low + (high - low) / 2
            count = sum(i <= mid for i in nums)
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low

# O(n) time
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1: return -1
        fast, slow = nums[nums[0]], nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        
        fast = 0
        while fast != slow:
            fast, slow = nums[fast], nums[slow]
        return slow
