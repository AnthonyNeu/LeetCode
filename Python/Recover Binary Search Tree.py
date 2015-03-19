"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#O(n) space solution, using in order traversal.
class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        stack = []
        result = []
        node = root
        while node or len(stack)>0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node)
                node = node.right
                
        prev = None
        first = None
        second = None
        idx = 0
        for i in range(len(result)):
            if prev is None:
                prev = result[i]
            elif first is None and prev.val >= result[i].val:
                first = prev
                idx = i
            elif first and prev.val >= result[i].val:
                second = result[i]
            prev = result[i]
        
        if second is None:
            second = result[idx]
            
        first.val,second.val = second.val,first.val

#O(n) space, in order traversal, using recursion to solve.
class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    prev = None
    first = None
    second = None
    def recoverTree(self, root):
        self.inOrderTraversal(root)
        self.first.val,self.second.val = self.second.val,self.first.val
        
    def inOrderTraversal(self,root):
        if root is None:
            return
        self.inOrderTraversal(root.left)
        if self.prev and self.prev.val > root.val:
            if self.first is None:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inOrderTraversal(root.right)

#O(1) space, Morris Traversal.
class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        self.MorrisTraversal(root)
    
    def MorrisTraversal(self, root):
        if root is None:
            return
        broken = [None, None]
        pre, cur = None, root
        
        while cur:
            if cur.left is None:
                self.detectBroken(broken, pre, cur)
                pre = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
                    
                if node.right is None:
                    node.right =cur
                    cur = cur.left
                else:
                    self.detectBroken(broken, pre, cur)
                    node.right = None
                    pre = cur
                    cur = cur.right
        
        broken[0].val, broken[1].val = broken[1].val, broken[0].val
    
    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur
