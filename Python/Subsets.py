"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
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
            result.append(tmp)
        return result

class Solution2:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        return self.subsetsRecu([], sorted(S))
    
    def subsetsRecu(self, cur, S):
        if len(S) == 0:
            return [cur]
        
        return self.subsetsRecu(cur, S[1:]) + self.subsetsRecu(cur + [S[0]], S[1:])