"""
Gray Code:
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

"""
Suppose we have already solved the problem for n-1 as input. We only need to add 1 to the MSB of the answer of n-1. We use the middle(in this example, it is 5) as the axis of symmetry.
"""
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        self.res = [0]
        for i in [2**x for x in range(0, n)]:
            self.res.append(self.res[-1] + i)
            self.res.extend([i + v for v in self.res[-3::-1]])
        return self.res