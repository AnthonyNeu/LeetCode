"""
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = []
        node = root
        result = []
        while len(stack) >0 or node is not None:
            if node is not None:
                result.append(node.val)
                if node.right is not None:
                    stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        return result

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        if root is not None:
            result.append(root.val)
            result += self.preorderTraversal(root.left)
            result += self.preorderTraversal(root.right)
        return result