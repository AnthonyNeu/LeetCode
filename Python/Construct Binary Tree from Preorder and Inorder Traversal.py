"""
Given preorder and inorder traversal of a tree, construct the binary tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder.pop(0))
        stn = list()
        stn.append(root)

        while True:
            if inorder[0] == stn[-1].val:
                p = stn.pop()
                inorder.pop(0)
                if len(inorder) == 0: break
                if len(stn) != 0 and inorder[0] == stn[-1].val: continue
                p.right = TreeNode(preorder.pop(0))
                stn.append(p.right)
            else:
                p = TreeNode(preorder.pop(0))
                stn[-1].left = p
                stn.append(p)

        return root
