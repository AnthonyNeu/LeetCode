"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy = ListNode(-9223372036854775807-1)
        dummy.next = head
        prev = dummy
        current = dummy
        while current and current.next and prev.next:
            if current.next.val >= x:
                current = current.next
            elif prev.next is not current.next:
                # remove current.next
                insert = current.next
                current.next = insert.next
                # put insert into the next of prev
                store = prev.next
                prev.next = insert
                insert.next = store
                # move pointer
                prev = prev.next
            else:
                current = current.next
                prev = prev.next
        return dummy.next

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        node1 = ListNode(0)
        node2 = ListNode(0)
        p1 = node1
        p2 = node2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = node2.next
        return node1.next
