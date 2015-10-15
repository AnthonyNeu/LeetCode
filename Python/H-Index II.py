"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
"""

class Solution1(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, result = 0, len(citations) - 1, 0
        while left <= right:
            mid = left + (right - left) / 2
            if citations[mid] <= len(citations) - mid:
                result = max(result, citations[mid])
                left = mid + 1
            else:
                result = max(result, len(citations) - mid)
                right = mid - 1
        return result

class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid - 1
        return len(citations) - right - 1
        