"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution:
    # @param height, an integer[]
    # @return an integer
    def trap(self, height):
        if len(height) == 0:
            return 0
        maxLeft = [0 for _ in xrange(len(height))]
        maxRight = [0 for _ in xrange(len(height))]
        maxLeft[0],maxRight[-1] = height[0],height[-1]
        for i in xrange(1,len(height)):
            maxLeft[i] = max(height[i],maxLeft[i-1])
            maxRight[-i] = max(height[-i],maxRight[-i+1])
            
        result = 0
        for i in xrange(1,len(height)):
            result += min(maxLeft[i],maxRight[i]) - height[i]
        return result