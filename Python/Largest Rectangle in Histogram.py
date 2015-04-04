"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

#Time O(n^2)
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        res = 0
        
        for i in reversed(xrange(len(height))):
            if i == len(height) - 1 or height[i] > height[i+1]:
                Min = 9223372036854775807
                
                for j in reversed(xrange(i+1)):
                    Min = min(Min,height[j])
                    res = max(res,(i+1-j)*Min)
        
        return res

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height) == 0 or height is None:
            return 0
        
        res = 0
        index = [-1]
        
        for i in range(len(height)):
            while index[-1] > -1:
                if height[index[-1]] > height[i]:
                    top = index.pop()
                    res = max(res,height[top] * (i - 1 - index[-1]))
                else:
                    break
            index.append(i)
        
        while index[-1] != -1:
            top = index.pop()
            res = max(res,height[top] * (len(height) - 1 - index[-1]))
        return res