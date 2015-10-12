"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num / 10 > 0:
            cur = str(num)
            next_num = 0
            for i in range(len(cur)):
                next_num += int(cur[i])
            num = next_num
        return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        return 1 + (num - 1) % 9
