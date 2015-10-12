"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        idx, low = -1, float('-inf')
        for p in preorder:
            if p < low:
                return False
            while idx >= 0 and p > preorder[idx]:
                low = preorder[idx]
                idx -= 1
            idx += 1
            preorder[idx] = p
        return True

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float('-inf')
        stack = []
        
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True
