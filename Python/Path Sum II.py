"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self.pathSumRecu([],[],root,sum)
        
    def pathSumRecu(self, result, cur, root, sum):
        if root is None:
            return result
        
        if root.left is None and root.right is None and root.val == sum:
            result.append(cur + [root.val])
            return result
        
        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, sum - root.val)
        self.pathSumRecu(result, cur,root.right, sum - root.val)
        cur.pop()
        return result

class Solution:
# @param root, a tree node
# @param S, an integer
# @return a list of lists of integers
    def pathSum(self, root, S):
        ret = []
        stack = []
        stack.append((root, []))
        while not stack == []:
            s = stack.pop()
            n, vs = s
            # empty tree wtf
            if n is None:
                continue
            l = n.left
            r = n.right
            v = sum(vs)
            # negative values
            #if n.val + v > S:
            #    continue
            vs = vs + [n.val]
            if l is None and r is None:
                if n.val + v == S:
                    ret.append(vs)
            if r is not None:
                stack.append((r, vs))
            if l is not None:
                stack.append((l, vs))
        return ret
