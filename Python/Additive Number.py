"""
Additive number is a positive integer whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string represents an integer, write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) < 3:
            return False
        n = len(num)
        
        def helper(idx, current):
            if idx == n:
                return True
            # if it is 0, we must add it as one number
            if num[idx] == '0':
                return helper(idx + 1, current + [0]) if len(current) <= 1 else False
            if not current or len(current) == 1:
                for i in range(1, (n - idx) / 2 + 1):
                    if helper(i + idx, current + [int(num[idx:i + idx])]):
                        return True
                return False
            else:
                target = current[-1] + current[-2]
                target_length = len(str(target))
                if n - idx < target_length or int(num[idx:target_length + idx]) != target:
                    return False
                return helper(target_length + idx, current + [target])
        return helper(0, [])
