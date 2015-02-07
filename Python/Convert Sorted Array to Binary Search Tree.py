"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        elif len(num) == 1:
            return TreeNode(num[0])
        elif len(num) == 2:
            root = TreeNode(num[1])
            root.left = TreeNode(num[0])
            return root
        elif len(num) == 3:
            root = TreeNode(num[1])
            root.left = TreeNode(num[0])
            root.right = TreeNode(num[2])
            return root
        
        
        mid = len(num) /2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root
