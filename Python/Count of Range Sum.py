"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""

# O(n logn) solution
# http://algobox.org/count-of-range-sum/
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        length = len(nums)
        sums = [0 for _ in range(length + 1)]
        for i in range(length):
            sums[i + 1] = nums[i] + sums[i]

        def helper(start, end):
            if end - start <= 1:
                return 0
            mid = start + (end - start) / 2
            count = helper(start, mid) + helper(mid, end)
            idx1 = lo = hi = mid
            """
            idx1, idx2 are two pointers used in merge sort
            """
            idx2 = 0
            sorted_cache = [0] * (end - start)
            for i in range(start, mid):
                while lo < end and sums[lo] - sums[i] < lower:
                    lo += 1
                while hi < end and sums[hi] - sums[i] <= upper:
                    hi += 1
                count += hi - lo
                # do the merge sort
                while idx1 < end and sums[idx1] < sums[i]:
                    sorted_cache[idx2] = sums[idx1]
                    idx1, idx2 = idx1 + 1, idx2 + 1
                sorted_cache[idx2] = sums[i]
                idx2 += 1
            sums[start:idx1] = sorted_cache[:idx1 - start]
            return count
        return helper(0, length + 1)

# O(n (log n) ^ 2) time
# https://leetcode.com/discuss/79907/summary-divide-conquer-based-binary-indexed-based-solutions
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0

        def helper(left, right):
            if left == right:
                return 1 if lower <= nums[left] <= upper else 0
            mid = left + (right - left) / 2
            sorted_cache = [0] * (right - mid)
            count, accu_sum = 0, 0
            for i in range(mid + 1, right + 1):
                accu_sum += nums[i]
                sorted_cache[i - mid - 1] = accu_sum
            sorted_cache.sort()
            accu_sum = 0
            for i in range(mid, left - 1, -1):
                accu_sum += nums[i]
                """
                search for idx1, idx2 in sorted_cache:
                sorted_cache[idx1] > upper - accu_sum
                sorted_cache[idx2] >= lower - accu_sum
                """
                count += self.binary_search(sorted_cache, upper - accu_sum + 0.5) - self.binary_search(sorted_cache, lower - accu_sum - 0.5)
            return helper(left, mid) + helper(mid + 1, right) + count
        return helper(0, len(nums) - 1)

    """
    find the largest index which arr[index] <= val
    """
    def binary_search(self, arr, val):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid] <= val:
                left = mid + 1
            else:
                right = mid - 1
        return left
