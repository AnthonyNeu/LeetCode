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

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)