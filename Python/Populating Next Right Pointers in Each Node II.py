"""
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?
Note:
You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return None
        # start TreeNode of a level
        parent = root
        # TreeNode which children are being searched for valid next TreeNode
        cur = root
        # TreeNode waiting to find the next TreeNode
        prev = None
        while cur:
            if prev is None:  # we need find valid perv TreeNode
                if cur.left and cur.right:
                    cur.left.next = cur.right
                    prev = cur.right
                elif cur.left:
                    prev = cur.left
                elif cur.right:
                    prev = cur.right

                # if we are in the end of this level,we need go to next level
                if cur.next:
                    cur = cur.next
                else:
                    prev = None
                    cur, parent = self.findNextValidNode(parent)
            else:  # we need find a valid next TreeNode
                if cur.left and cur.right:
                    prev.next = cur.left
                    cur.left.next = cur.right
                    prev = cur.right
                elif cur.left:
                    prev.next = cur.left
                    prev = prev.next
                elif cur.right:
                    prev.next = cur.right
                    prev = prev.next

                # if we are in the end of this level,we need go to next level
                if cur.next:
                    cur = cur.next
                else:
                    prev = None
                    cur, parent = self.findNextValidNode(parent)
        return root
        
    # find the next level's first valid TreeNode
    def findNextValidNode(self, parent):
        cur = None
        while parent and parent.left is None and parent.right is None:
            parent = parent.next

        if parent is None:
            return cur, None
        else:
            if parent.left:
                parent = parent.left
                cur = parent
            else:
                parent = parent.right
                cur = parent
        return cur, parent

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right
                
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left
                    
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right
                    
                cur = cur.next
            head = next_head

# recursion version
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        dummy = TreeLinkNode(-1)
        prev, cur = dummy, root
        while cur:
            if cur.left:
                prev.next = cur.left
                prev = prev.next
            if cur.right:
                prev.next = cur.right
                prev = prev.next
            cur = cur.next
        self.connect(dummy.next)
