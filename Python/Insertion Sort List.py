"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return None

        dummy = ListNode(-9223372036854775807-1)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.val < cur.next.val:
                cur = cur.next
            else:
                insert = cur.next
                cur.next = insert.next
                start = dummy
                prev = start
                while start.val < insert.val:
                    prev = start
                    start = start.next
                prev.next = insert
                insert.next = start
        return dummy.next
