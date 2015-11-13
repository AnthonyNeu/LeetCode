"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
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
    Max = float('-inf')
    def maxPathSum(self, root):
        self.maxPathSumHelper(root,self.Max)
        return self.Max
    
    def maxPathSumHelper(self,root,Max):
        if root is None:
            return 0
        l = max(0,self.maxPathSumHelper(root.left,self.Max))
        r = max(0,self.maxPathSumHelper(root.right,self.Max))
        self.Max = max(self.Max,l+r+root.val)
        return root.val + max(l,r)
