"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        
        l1,l2 = self.splitList(head)
        
        sorted_l1 = self.sortList(l1)
        sorted_l2 = self.sortList(l2)
        
        return self.mergeList(sorted_l1,sorted_l2)
        
        
    def splitList(self,head):
        if head is None:
            return None
        fast = head
        slow = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head,slow

    def mergeList(self,l1,l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next,current,l1 = l1,l1,l1.next
            else:
                current.next,current,l2 = l2,l2,l2.next  #Notice: don't do current = current.next here
                                                         #As current.next is l2, which will be assigned to l2.next after    
        if l1:
                current.next = l1
        elif l2:
                current.next = l2
        return dummy.next
