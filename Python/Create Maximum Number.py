"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""

# https://leetcode.com/discuss/75756/share-my-greedy-solution
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        if k > m + n:
            return [0] * k
        result = [0] * k
        for i in range(max(0, k - n), min(k + 1, m + 1)):
            candidate = self.merge(self.generate_max_array(nums1, i), self.generate_max_array(nums2, k - i), k)
            if self.compare(candidate, result, 0, 0):
                result = candidate
        return result

    def generate_max_array(self, nums, length):
        """
        generate a maximum subsequence of array with length.
        """
        ans, l, j = [0] * length, len(nums), 0
        for i in range(l):
            while l - i + j > length and j > 0 and ans[j - 1] < nums[i]:
                j -= 1
            if j < length:
                ans[j] = nums[i]
                j += 1
        return ans

    def compare(self, nums1, nums2, i, j):
        """
        compare two arrays start from i, j.
        if elements in nums1 are larger than nums2, return true.
        else return false.
        """
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i, j = i + 1, j + 1
        return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

    def merge(self, nums1, nums2, k):
        """
        pick elements from nums1 and nums2 to get a maximum array of size k. The total size of nums1 and nums2 is k.
        """
        ans = [0] * k
        i, j = 0, 0
        for r in range(k):
            if self.compare(nums1, nums2, i, j):
                ans[r] = nums1[i]
                i += 1
            else:
                ans[r] = nums2[j]
                j += 1
        return ans
