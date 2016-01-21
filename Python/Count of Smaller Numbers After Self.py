"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""

class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        segment_tree, result, cur_min = self.build(min(nums), max(nums)), [], float('inf')
        for i in reversed(range(len(nums))):
            answer = 0
            if i == len(nums) - 1 or cur_min > nums[i]:
                cur_min = nums[i]
            else:
                answer = self.query(segment_tree, cur_min, nums[i] - 1)
            result.append(answer)
            self.modify(segment_tree, nums[i], 1)
        return result[::-1]

    def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, 0)
        if start != end:
            mid = start + (end - start) / 2
            root.left = self.build(start, mid)
            root.right = self.build(mid + 1, end)
        else:
            root.count = 0
        return root

    def query(self, root, start, end):
        if start > end or not root:
            return 0
        if start <= root.start and root.end <= end:
            return root.count
        mid = root.start + (root.end - root.start) / 2
        left_sum, right_sum = 0, 0
        if start <= mid:
            if mid < end:
                left_sum = self.query(root.left, start, mid)
            else:
                left_sum = self.query(root.left, start, end)
        if mid < end:
            if start <= mid:
                right_sum = self.query(root.right, mid + 1, end)
            else:
                right_sum = self.query(root.right, start, end)
        return left_sum + right_sum

    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.count += value
            return
        mid = root.start + (root.end - root.start) /2
        if index >= root.start and index <= mid:
            self.modify(root.left, index, value)
        elif index >= mid + 1 and index <= root.end:
            self.modify(root.right, index, value)
        root.count = root.left.count + root.right.count

# using binary indexed tree
class Solution(object):
    BITree = []
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        sorted_nums = list(nums)
        sorted_nums.sort()
        """
        find the insertion place for every element in the array
        using the insertion place as the index to insert to BIT
        """
        move = [self.searchInsert(sorted_nums, nums[i]) + 1 for i in range(length)]
        self.BITree = [0 for _ in range(length + 1)]
        result = [0 for _ in range(length)]
        for i in range(length - 1, -1, -1):
            result[i] = self.query(move[i] - 1)
            self.add(move[i], 1)
        return result

    def add(self, idx, value):
        i = idx
        while i < len(self.BITree):
            self.BITree[i] += value
            i += i& (-i)

    def query(self, idx):
        result, i = 0, idx
        while i > 0:
            result += self.BITree[i]
            i -= i & (-i)
        return result

    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if target <= A[-1] else left + 1

# https://leetcode.com/discuss/73256/mergesort-solution
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum) - 1, -1, -1):
                    if not right or (left and left[-1][1] > right[-1][1]):
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
