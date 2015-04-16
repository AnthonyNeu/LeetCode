"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Divide and Conquer
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        while len(lists) >= 2:
            newList = []
            for i in xrange(len(lists)/2):
                newList.append(self.mergeTwoLists(lists.pop(),lists.pop(0)))
            if len(lists) > 0 :
                newList.append(lists.pop())
            lists = newList
        return lists.pop()
        
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2=l2.next
                head = head.next
            else:
                head.next = l1
                l1=l1.next
                head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        else:
            head.next = None
        return dummy.next

# Priority Queue
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        
        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))
                
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
                
        return dummy.next