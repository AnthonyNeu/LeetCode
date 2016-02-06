"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""


# https://leetcode.com/discuss/83825/simple-python-solution-using-stack-with-explanation
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        top = -1
        preorder = preorder.split(',')

        """
        this function is for checking whether the last
        two elements in the stack are both "#".
        """
        def is_end_with_two_hashes():
            if top < 1:
                return False
            if stack[top] == stack[top - 1] == '#':
                return True
            return False
        for s in preorder:
            stack.append(s)
            top += 1
            while is_end_with_two_hashes():
                # remove two #
                stack.pop()
                stack.pop()
                top -= 2
                if top < 0:
                    return False
                # remove the parent
                stack.pop()
                stack.append('#')
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False


# https://leetcode.com/discuss/83809/simple-o-n-solution
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        preorder = preorder.split(',')
        idx = depth = 0
        length = len(preorder)
        while idx < length - 1:
            if preorder[idx] == '#':
                if depth == 0:
                    return False
                depth -= 1
            else:
                depth += 1
            idx += 1
        if depth != 0:
            return False
        return preorder[-1] == '#'

# https://leetcode.com/discuss/83824/7-lines-easy-java-solution
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        diff = 1
        for s in preorder:
            if diff - 1 < 0:
                return False
            diff -= 1
            if s != '#':
                diff += 2
        return diff == 0
