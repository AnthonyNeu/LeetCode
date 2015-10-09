"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        result = []
        idx = 0
        while idx < len(input):
            if not input[idx].isdigit():
                ans1 = self.diffWaysToCompute(input[:idx])
                ans2 = self.diffWaysToCompute(input[idx + 1:])
                for i in xrange(len(ans1)):
                    for j in xrange(len(ans2)):
                        result.append(self.compute(ans1[i], ans2[j], input[idx]))
            idx += 1
        return result
        
    def compute(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        else:
            return num1 * num2
