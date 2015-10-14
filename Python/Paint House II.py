"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""
# Time:  O(n * k)
# Space: O(1)
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0:
            return 0
        
        n, k = len(costs), len(costs[0])
        
        min1 = min2 = -1
        
        for i in range(n):
            last1, last2 = min1, min2
            min1 = min2 = -1
            
            for j in range(k):
                if j != last1:
                    costs[i][j] += 0 if last1 < 0 else costs[i - 1][last1]
                else:
                    costs[i][j] += 0 if last2 < 0 else costs[i - 1][last2]
                
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[n - 1][min1]

# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        return min(reduce(self.combine, costs)) if costs else 0

    def combine(self, tmp, house):
        smallest, k, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp, tmp[i] = [smallest] * k, min(tmp[:i] + tmp[i+1:])
        return map(sum, zip(tmp, house))
