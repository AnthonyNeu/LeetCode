"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        solutions = [[]]
        
        for number in num:
            next = []
            for solution in solutions:
                for i in xrange(len(solution)+1):
                    candidate = solution[:i] + [number] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions


class Solution:
    # @param num, a list of integer 
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num) == 0:
            return []
        result = []
        used = [False] * len(num)
        self.permuteRe(result,used,[],sorted(num))
        return result

    def permuteRe(self,result,used,current,num):
        if len(current) == len(num):
            result.append(current[:])
        prev_idx = -1
        for i in xrange(len(num)):
            if used[i] or (prev_idx != -1 and num[prev_idx] == num[i]):
                continue
            used[i] = True
            current.append(num[i])
            self.permuteRe(result,used,current,num)
            current.pop()
            used[i] = False
            prev_idx = i