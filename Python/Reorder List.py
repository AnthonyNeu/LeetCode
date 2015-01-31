"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You must do this in-place without altering the nodes' values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        
        a,b = self.splitList(head)
        b = self.reverseList(b)
        head = self.mergeList(a,b)
    
    # @param a, a ListNode
    # @param b, a ListNode
    # @return the merged list
    def mergeList(self,a,b):
        head = a
        tail = a
        
        while b:
            tmp = tail.next
            nextNode = b.next
            tail.next = b
            tail.next.next = tmp
            b = nextNode
            tail = tail.next.next
        return head
        
    # @param head,a ListNode
    # @return head, a ListNode which is the first half of head
    # @returm middle, a ListNode which begin from the end of head to the middle of head
    def splitList(self,head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return head,middle
        
    # return last, a reversed List of head
    def reverseList(self,head):
        if head is None:
            return None
        
        current = head
        last = None
        while current:
            tmp = current.next
            current.next = last
            last = current
            current = tmp
        return last
