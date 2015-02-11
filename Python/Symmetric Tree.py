"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
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
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None and root:
            return True
        if root.right and root.left:
            if root.right.val != root.left.val:
                return False
        else:
            return False
        forward = [root.left]
        backward = [root.right]
        while len(forward) > 0:
            forward_new =[]
            backward_new = []
            while len(forward) >0:
                node1 = forward.pop()
                node2 = backward.pop()
                
                # case 1: all have left subtree and right subtree
                if node1.left and node1.right and node2.left and node2.right:
                    if node1.left.val == node2.right.val and node1.right.val == node2.left.val:
                        forward_new.append(node1.left)
                        forward_new.append(node1.right)
                        backward_new.append(node2.right)
                        backward_new.append(node2.left)
                    else:
                        return False
                # case 2: one has left and one has right
                elif node1.left and node2.right and node1.right is None and node2.left is None:
                    if node1.left.val != node2.right.val:
                        return False
                    forward_new.append(node1.left)
                    backward_new.append(node2.right)
                elif node2.left and node1.right and node1.left is None and node2.right is None:
                    if node2.left.val != node1.right.val:
                        return False
                    forward_new.append(node1.right)
                    backward_new.append(node2.left)
                # case 3: no subtree
                elif node1.left is None and node1.right is None and node2.left is None and node2.right is None:
                    return True
                else:
                    return False
            forward = forward_new
            backward = backward_new
        return True

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricHelper(root.left,root.right)
        
    def isSymmetricHelper(self,left,right):
        if left is None and right is None:
            return True
        elif left and right:
            if left.val == right.val:
                return self.isSymmetricHelper(left.left,right.right) and self.isSymmetricHelper(left.right,right.left)
            else:
                return False
        else:
            return False