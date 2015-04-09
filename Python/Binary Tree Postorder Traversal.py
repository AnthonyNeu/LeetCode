"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time:  O(n)
# Space: O(n)
# Stack Solution 
class Solution:
    def __init__(self):
        self.result = []
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        parent = []
        lastvisit = None
        
        while parent or root:
            if root:
                parent.append(root)
                root = root.left
            else:
                peeknode = parent[-1]
                # if right child exists and traverse from the left child,move right
                if peeknode.right and lastvisit is not peeknode.right:
                    root = peeknode.right
                else:
                    self.result.append(peeknode.val)
                    lastvisit = parent.pop()
        
        return self.result


# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [], dummy
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
            
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right
        
        return result
    
    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur is not to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result