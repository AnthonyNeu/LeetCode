"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = []
        self.subsetsWithDupRecu(result, [], sorted(S))
        return result
    
    def subsetsWithDupRecu(self, result, cur, S):
        if len(S) == 0  and cur not in result:
            result.append(cur)
        elif S:
            self.subsetsWithDupRecu(result, cur, S[1:])
            self.subsetsWithDupRecu(result, cur + [S[0]], S[1:])

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if len(S) == 0:
            return [[]]
        num = 2 ** len(S)
        result = []
        for i in range(num):
            tmp = []
            idx = 0
            j = i
            while j > 0:
                if j & 1:
                    tmp.append(S[idx])
                idx +=1
                j >>=1
            tmp = sorted(tmp)
            if tmp not in result:
                result.append(tmp)
        return result