"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.getFactorsRecu(result, [], n)
        return result
    
    def getFactorsRecu(self, result, current, target):
        factor = 2 if not current else current[-1]
        while factor <= (target / factor):
            if target % factor == 0:
                current.append(factor)
                current.append(target / factor)
                result.append(list(current))
                current.pop()
                self.getFactorsRecu(result, current, target / factor)
                current.pop()
            factor += 1
