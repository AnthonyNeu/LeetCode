"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def jump(self, nums):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last:
                # if not last one and can't go further
                if (curr == last) and (last < len(nums)-1):
                    return -1   # never reach the last one
                last = curr
                ret += 1
            curr = max(curr, i+nums[i])
        return ret