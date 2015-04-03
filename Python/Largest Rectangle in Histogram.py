"""

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