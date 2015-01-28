"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        N = len(num)
        num = sorted(num)
        ret = sum(num[:3])
        for i in range(N-2):
            l = i+1
            r = N-1
            while l < r:
                threesum = num[l]+num[r]+num[i]
                if abs(target - threesum) < abs(target - ret):
                    ret = threesum
                elif threesum == target:
                    return threesum
                elif threesum < target:
                    l += 1
                else:
                    r -=1
        return ret
