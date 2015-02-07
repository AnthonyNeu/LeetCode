"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root):
        if root is None:
            return 0
            
        if root.left and root.right:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        elif root.left:
            return 1+self.minDepth(root.left)
        elif root.right:
            return 1+self.minDepth(root.right)
        else:
            return 1