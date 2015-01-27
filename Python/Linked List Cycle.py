"""
Linked List Cycle
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        lookup = {}
        while head.next:
            if lookup.has_key(head):
                return True
            else:
                lookup[head]=True
                head = head.next
        return False

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                return True
        return False