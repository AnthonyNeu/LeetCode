"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return root
        stack = []
        while root.left:
            stack.append(root)
            tmp = root.left
            root.left = None
            root = tmp
        dummy = TreeNode(-1)
        dummy.right = root
        cur = root
        while stack:
            node = stack.pop()
            if node.right:
                tmp = node.right
                node.right = None
                cur.left = tmp
            cur.right = node
            cur = cur.right
        return dummy.right

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        prev = None
        # store the right node
        temp = None
        next = None
        
        while cur:
            next = cur.left
            cur.left = temp
            temp = cur.right
            cur.right = prev
            prev = cur
            cur = next
        
        return prev
