"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

# Heap: O(Nlogk) time, O(1) space
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        

# Quick Select:O(N) time, O(1) space
from random import randint

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        left,right = 0,len(nums)-1
        while left <= right:
            pivotIdx = randint(left,right)
            newPivotIdx = self.partition(left,right,pivotIdx,nums)
            if newPivotIdx == k-1:
                return nums[newPivotIdx]
            elif newPivotIdx > k-1:
                right = newPivotIdx -1
            else:
                left = newPivotIdx + 1
        
    def partition(self,left,right,pivotIdx,nums):
        pivot = nums[pivotIdx]
        nums[pivotIdx],nums[right] = nums[right],nums[pivotIdx]
        storeIdx = left
        for i in xrange(left,right):
            if nums[i] > pivot:
                nums[storeIdx],nums[i] = nums[i],nums[storeIdx]
                storeIdx +=1
        nums[right],nums[storeIdx] = nums[storeIdx],nums[right]
        return storeIdx