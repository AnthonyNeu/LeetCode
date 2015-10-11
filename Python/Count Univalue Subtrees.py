# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        is_uni, count = self.countUnivalSubtreesRecu(root)
        return count

    def countUnivalSubtreesRecu(self, root):
        if root is None: return [True, 0]
        if root.left is None and root.right is None: return [True, 1]
        if root.left is None or root.right is None:
            is_uni, count = self.countUnivalSubtreesRecu(root.right if root.right else root.left)
            if is_uni and (root.right.val == root.val if root.right else root.left.val == root.val):
                return [True, count + 1]
            else:
                return [False, count]
        is_left_uni, left_count = self.countUnivalSubtreesRecu(root.left)
        is_right_uni, right_count = self.countUnivalSubtreesRecu(root.right)
        if root.right.val == root.left.val and root.val == root.left.val and is_left_uni and is_right_uni:
            return [True, left_count + right_count + 1]
        else:
            return [False, left_count + right_count]


# a clean version
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        is_uni, count = self.countUnivalSubtreesRecu(root)
        return count

    def countUnivalSubtreesRecu(self, root):
        if root is None: return [True, 0]
        
        is_left_uni, left_count = self.countUnivalSubtreesRecu(root.left)
        is_right_uni, right_count = self.countUnivalSubtreesRecu(root.right)
        if self.isSame(root, root.left, is_left_uni) and self.isSame(root, root.right, is_right_uni):
            return [True, left_count + right_count + 1]
        else:
            return [False, left_count + right_count]
            
    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)
