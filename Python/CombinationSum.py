"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecur(sorted(candidates), result, [], 0, target)
        return result
        
    def combinationSumRecur(self, candidates, result, current, start, target):
        if target == 0:
            result.append(current)
        else:
            while start < len(candidates) and candidates[start] <= target:
                self.combinationSumRecur(candidates, result, current + [candidates[start]], start, target - candidates[start])
                start += 1