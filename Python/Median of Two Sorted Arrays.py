"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 0:
            return ( self.findKth(A, 0, B, 0, length / 2) + self.findKth(A, 0, B, 0, length / 2 + 1) ) / 2.0
        else:
            return self.findKth(A, 0, B, 0, length / 2 + 1)

    def findKth(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            return B[B_start + k - 1]
        if B_start >= len(B):
            return A[A_start + k - 1]

        if k == 1:
            return min(A[A_start], B[B_start])

        if A_start + k/2 -1 < len(A):
            A_key = A[A_start + k/2 -1]
        else:
            A_key = 9223372036854775807

        if B_start + k/2 -1 < len(B):
            B_key = B[B_start + k/2 -1]
        else:
            B_key = 9223372036854775807

        if A_key < B_key:
            return self.findKth(A, A_start + k / 2, B, B_start, k - k/2)
        else:
            return self.findKth(A, A_start, B, B_start + k / 2, k - k/2)

# https://leetcode.com/discuss/41621/very-concise-iterative-solution-with-detailed-explanation
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2:
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
        l, r = 0, N2*2
        while l <= r:
            j = (l + r) >> 1
            i = N1 + N2 - j
            L1 = -sys.maxint-1 if i == 0 else nums1[(i-1)>>1]
            L2 = -sys.maxint-1 if j == 0 else nums2[(j-1)>>1]
            R1 = sys.maxint if i == 2*N1 else nums1[i>>1]
            R2 = sys.maxint if j == 2*N2 else nums2[j>>1]
            if L1 > R2: l = j + 1
            elif L2 > R1: r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2.0
