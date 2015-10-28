"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

Hint:

Try to solve it in one dimension first. How can this solution apply to the two dimension case?
"""

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_sum = map(sum, grid)
        col_sum = map(sum, zip(*grid))
    
        def minTotalDistance1D(vec):
            size = len(vec)
            left, right = -1, size
            count_l, count_r = 0, 0
            while left < right:
                if count_l < count_r:
                    left += 1
                    count_l += vec[left]
                else:
                    right -= 1
                    count_r += vec[right]
        
            # median is right (left)
            dis = 0
            for i in xrange(size):
                dis += vec[i] * abs(i - left)
            return dis
    
        return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)
