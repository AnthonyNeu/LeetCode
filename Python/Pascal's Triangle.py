"""
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows ==0:
            return []
        list = [[1]]
        for i in range(1,numRows):
            row = []
            previous = list[i-1]
            for j in range(i+1):
                if j == 0:
                    row.append(previous[j])
                elif j == i:
                    row.append(previous[j-1])
                else:
                    row.append(previous[j-1]+previous[j])
            list.append(row)
        return list