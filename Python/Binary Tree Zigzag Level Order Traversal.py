"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        queue = []
        if root is None:
            return []
        result = []
        queue.append(root)
        case = 0
        while len(queue)>0:
            n = len(queue)
            visit = []
            while n > 0:
                n -=1
                node = queue.pop(0)
                if case == 0:
                    visit.append(node.val)
                else:
                    visit.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            case ^=1
            result.append(visit)
        return result