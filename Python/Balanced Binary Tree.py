"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        
        result1 = self.isBalanced(root.left)
        result2 = self.isBalanced(root.right)
        
        if result1 and result2 and abs(self.TreeHeight(root.left) - self.TreeHeight(root.right)) <=1:
            return True
        else:
            return False
        
    def TreeHeight(self,root):
        height = 0
        
        if root:
            height1 = self.TreeHeight(root.left)
            height2 = self.TreeHeight(root.right)
            height =max(height1,height2) + 1
        return height

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.isBalanced_1(root)

    def isBalanced_1(self, root):
        if root is None:
            return True
        if self.get_height(root) == -1:
            return False
        return True

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1