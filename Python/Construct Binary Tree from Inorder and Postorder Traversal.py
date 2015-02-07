"""
Construct Binary Tree from Postorder and Inorder Traversal.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        stn = list()
        stn.append(root)

        while True:
            if inorder[-1] == stn[-1].val:
                p = stn.pop()
                inorder.pop()
                if len(inorder) == 0: break
                if len(stn) != 0 and inorder[-1] == stn[-1].val: continue
                p.left = TreeNode(postorder.pop())
                stn.append(p.left)
            else:
                p = TreeNode(postorder.pop())
                stn[-1].right = p
                stn.append(p)

        return root
