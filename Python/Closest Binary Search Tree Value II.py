"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

Consider implement these two helper functions:
getPredecessor(N), which returns the next smaller node to N.
getSuccessor(N), which returns the next larger node to N.
Try to assume that each node has a parent pointer, it makes the problem much easier.
Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
You would need two stacks to track the path in finding predecessor and successor node separately.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use inorder traversal
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        predecessor, successor = [], []
        
        root_left, root_right  = lambda root : root.left, lambda root : root.right
        self.getPath(predecessor, target, root, root_right, root_left, lambda x : x <= target)
        self.getPath(successor, target, root, root_left, root_right, lambda x : x > target)
        
        result = []
        while k > 0:
            if not predecessor:
                result.append(successor.pop())
            elif not successor:
                result.append(predecessor.pop())
            elif abs(predecessor[-1] - target) > abs(successor[-1] - target):
                result.append(successor.pop())
            else:
                result.append(predecessor.pop())
            k -= 1
        return result
            
    def getPath(self, stack, target, root, root_left, root_right, condition):
        if root is None: return
        self.getPath(stack, target, root_left(root), root_left, root_right, condition)
        if condition(root.val): return
        stack.append(root.val)
        self.getPath(stack, target, root_right(root), root_left, root_right, condition)

# calculate the path to the next node in the tree
class Solution2(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Helper, takes a path and makes it the path to the next node
        def nextpath(path, kid1, kid2):
            if path:
                if kid2(path):
                    path += kid2(path),
                    while kid1(path):
                        path += kid1(path),
                else:
                    kid = path.pop()
                    while path and kid is kid2(path):
                        kid = path.pop()
    
        # These customize nextpath as forward or backward iterator
        kidleft = lambda path: path[-1].left
        kidright = lambda path: path[-1].right
    
        # Build path to closest node
        path = []
        while root:
            path += root,
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target)
        path = path[:path.index(min(path, key=dist))+1]
    
        # Get the path to the next larger node
        path2 = path[:]
        nextpath(path2, kidleft, kidright)
    
        # Collect the closest k values by moving the two paths outwards
        vals = []
        for _ in range(k):
            if not path2 or path and dist(path[-1]) < dist(path2[-1]):
                vals += path[-1].val,
                nextpath(path, kidright, kidleft)
            else:
                vals += path2[-1].val,
                nextpath(path2, kidleft, kidright)
        return vals
