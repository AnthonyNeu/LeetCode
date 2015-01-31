"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None or k is 0:
            return head
        count = k
        p1 = head
        p2 = head
        prev = head
        while k > 0:
            p2 = p2.next
            k -=1
            if p2 is None and k >0:
                p2 = head
        if p2 is None:
            return head
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        prev.next = None
        dummy = ListNode(0)
        dummy.next = p1
        while p1.next:
            p1 = p1.next
        p1.next = head
        return dummy.next

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 1
        tail = head                     # Naming
        while tail.next:                # No need to use extra prev
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head                 # Detail
        tail.next = head
        cur = head
        i = 0
        while i < length - k - 1:       # Note this detail
            cur = cur.next
            i += 1
        new_head = cur.next
        cur.next = None
        return new_head
