"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Divide and Conquer
# Time O(n)
# Space O(n)
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []
        
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        
        result = [root.val]
        
        for i in xrange(max(len(left),len(right))):
            if i >= len(right):
                result.append(left[i])
            else:
                result.append(right[i])
        return result

# Reversed Level Order Traversal
# Time O(n)
# Space O(n)
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root is None:
            return []
        queue = []
        result = []
        
        queue.append(root)
        while len(queue) > 0:
            for i in xrange(len(queue)):
                cur = queue.pop(0)
                if i == 0:
                    result.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return result
                