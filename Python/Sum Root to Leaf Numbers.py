"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersHelper([],root)
        
    def sumNumbersHelper(self,stack,root):
        if root is None:
            return 0
        
        if root.right is None and root.left is None and root:
            N = len(stack)
            sumAll = 0
            for num in stack:
                sumAll += num * 10 ** N
                N -=1
            return sumAll + root.val
        
        stack.append(root.val)
        sum1 = self.sumNumbersHelper(stack,root.left)
        sum2 = self.sumNumbersHelper(stack,root.right)
        stack.pop()
        return sum1+sum2

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)
    
    def sumNumbersRecu(self, root, num):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return num * 10 + root.val
        
        return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)