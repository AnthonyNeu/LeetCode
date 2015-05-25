"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""



class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        self.combinationSumRecu(k,[],n,1,result)
        return result
    
    def combinationSumRecu(self,k,current,target,start,result):
        if k < 0:
            return
        if target == 0 and k == 0:
            result.append(current[:])
        for i in xrange(start,min(9,target)+1):
            if (target <= i * 2 and k > 1):
                continue
            current.append(i)
            self.combinationSumRecu(k-1,current,target - i,i+1,result)
            current.pop()