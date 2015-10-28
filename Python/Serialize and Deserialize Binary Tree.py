"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ''
        
        def serialize_helper(root):
            if not root:
                self.res += '# '
                return 
            else:
                self.res += str(root.val) + ' '
                serialize_helper(root.left)
                serialize_helper(root.right)
        serialize_helper(root)
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(" ")
        nodes.pop()
        self.res = None
        self.pointer = 0
        
        def deserialize_helper():
            if nodes[self.pointer] != '#':
                new_node = TreeNode(int(nodes[self.pointer]))
                if not self.res:
                    self.res = new_node
                self.pointer += 1
                new_node.left = deserialize_helper()
                new_node.right = deserialize_helper()
                return new_node
            else:
                self.pointer += 1
                return None
        deserialize_helper()
        return self.res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
