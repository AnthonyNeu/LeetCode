"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            self.sums.append(cur_sum)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - self.sums[i - 1] if i else self.sums[j]

class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start, self.end, self.sum = start, end, None
        self.left, self.right = None, None

# segment tree
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.segment_tree_root = self.build(0, len(nums) - 1, nums)

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

# binary indexed tree
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
# numArray.sumRange(1, 2)
