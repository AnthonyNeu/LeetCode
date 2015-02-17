"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        previous = [1]
        i = 1
        while i <= rowIndex:
            result = []
            for j in range(i+1):
                if j == 0:
                    result.append(previous[j])
                elif j == i:
                    result.append(previous[j-1])
                else:
                    result.append(previous[j-1]+previous[j])
            previous = result
            i +=1
        return result