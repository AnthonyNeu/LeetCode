"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start, self.end, self.sum = start, end, None
        self.left, self.right = None, None

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.segment_tree_root = self.build(0, len(nums) - 1, nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.modify(self.segment_tree_root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(self.segment_tree_root, i, j)
        
    def build(self, start, end, nums):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start != end:
            mid = start + (end - start) / 2
            root.left = self.build(start, mid, nums)
            root.right = self.build(mid + 1, end, nums)
            root.sum = root.left.sum + root.right.sum
        else:
            root.sum = nums[start]
        return root

    def query(self, root, start, end):
        if not root:
            return 0
        if root.start >= start and root.end <= end:
            return root.sum
        mid = root.start + (root.end - root.start) / 2
        left_sum, right_sum = 0, 0
        if start <= mid:
            if end > mid:
                left_sum = self.query(root.left, start, mid)
            else:
                left_sum = self.query(root.left, start, end)
        if end > mid:
            if start <= mid:
                right_sum = self.query(root.right, mid + 1, end)
            else:
                right_sum = self.query(root.right, start, end)
        return left_sum + right_sum
        
    def modify(self, root, index, val):
        if root.start == index and root.end == index:
            root.sum = val
            return
        mid = root.start + (root.end - root.start) /2
        if index >= root.start and index <= mid:
            self.modify(root.left, index, val)
        elif index >= mid + 1 and index <= root.end:
            self.modify(root.right, index, val)
        root.sum = root.left.sum + root.right.sum


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.BITree= [0] * (self.n + 1)
        for i in range(self.n):
            self._update_BIT(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.sumRange(i, i)
        self._update_BIT(i, delta)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._get_sum(j) - self._get_sum(i - 1)

    def _update_BIT(self, index, val):
        # index in BIT is one more than original nums
        index += 1
        # traverse all the ancestors of BITree[index]
        while index <= self.n:
            # add 'val' to current node of BI Tree
            self.BITree[index] += val
            # update index to its parent
            index += index & (-index)
        
    def _get_sum(self, index):
        # index in BIT is one more than original nums
        index += 1
        result = 0
        # traverse all the subtrees whose indexes are less than "index"
        while index > 0:
            # add current element of BITree to sum
            result += self.BITree[index]
            # update index to previous subtree
            index -= index & (-index)
        return result

# using 2D segment tree
class QuadTreeNode:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.mid_x = x1 + (x2 - x1) / 2
        self.mid_y = y1 + (y2 - y1) / 2
        self.sum = 0
        self.ul = None
        self.ur = None
        self.bl = None
        self.br = None

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix:
            return
        self.root = self._build(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        
    def _build(self, x1, y1, x2, y2):
        root = QuadTreeNode(x1, y1, x2, y2)
        if x1 == x2 and y1 == y2:
            root.sum = self.matrix[x1][y1]
        else:
            mid_x = x1 + (x2 - x1) / 2
            mid_y = y1 + (y2 - y1) / 2
            root.ul = self._build(x1, y1, mid_x, mid_y)
            root.sum += root.ul.sum
            if mid_y + 1 <= y2:
                root.ur = self._build(x1, mid_y + 1, mid_x, y2)
                root.sum += root.ur.sum
            if mid_x + 1 <= x2:
                root.bl = self._build(mid_x + 1, y1, x2, mid_y)
                root.sum += root.bl.sum
            if mid_x + 1 <= x2 and mid_y + 1 <= y2:
                root.br = self._build(mid_x + 1, mid_y + 1, x2, y2)
                root.sum += root.br.sum
        return root
    
    def _update(self, root, row, col, val):
        if root.x1 > row or root.x2 < row or root.y1 > col or root.y2 < col:
            return
        if root.x1 == root.x2 and root.x1 == row and root.y1 == root.y2 and root.y1 == col:
            root.sum = val
        else:
            root.sum = 0
            if row <= root.mid_x and col <= root.mid_y:
                self._update(root.ul, row, col, val)
                root.sum += root.ul.sum
            elif row <= root.mid_x and col > root.mid_y:
                self._update(root.ur, row, col, val)
                root.sum += root.ur.sum
            elif row > root.mid_x and col <= root.mid_y:
                self._update(root.bl, row, col, val)
                root.sum += root.bl.sum
            else:
                self._update(root.br, row, col, val)
                root.sum += root.br.sum
    
    def _query(self, root, row1, col1, row2, col2):
        if not root:
            return 0
        if root.x1 >= row1 and root.y1 <= col1 and root.x2 >= row2 and root.y2 <= col2:
            return root.sum
        result = 0
        if row1 <= root.mid_x and col1 <= root.mid_y:
            result += self._query(root.ul, row1, col1, row2, col2)
        if row1 <= root.mid_x and col2 > root.mid_y:
            result += self._query(root.ur, row1, col1, row2, col2)
        if row2 > root.mid_x and col1 <= root.mid_y:
            result += self._query(root.bl, row1, col1, row2, col2)
        if row2 > root.mid_x and col2 > root.mid_y:
            result += self._query(root.br, row1, col1, row2, col2)
        return result

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if not self.matrix:
            return
        self._update(self.root, row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        return self._query(self.root, row1, col1, row2, col2)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)