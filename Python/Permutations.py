"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        result = []
        used = [False] * len(num)
        self.permuteRe(result,used,[],num)
        return result
        
    def permuteRe(self,result,used,current,num):
        if len(current) == len(num):
            result.append(current[:])
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                current.append(num[i])
                self.permuteRe(result,used,current,num)
                current.pop()
                used[i] = False


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        solutions = [[]]
        
        for number in num:
            next = []
            for solution in solutions:
                for i in xrange(len(solution)+1):
                    candidate = solution[:i] + [number] + solution[i:]
                    next.append(candidate)
            solutions = next
        return solutions