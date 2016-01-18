"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        odd, even, cur = head, head.next, head.next.next
        while cur:
            p1, p2 = odd.next, cur.next
            # add cur to the end of odd
            odd.next = cur
            cur.next = p1
            even.next = p2
            # move odd and even to next node
            odd = odd.next
            even = even.next
            if even:
                cur = even.next
            else:
                break
        return head


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd = head
            even = even_head = odd.next
            while even and even.next:
                odd.next = odd = even.next
                even.next = even = odd.next
            odd.next = even_head
        return head

# XOR solution
# https://leetcode.com/discuss/80370/xor-solution-and-shortened-other-c-java-python
def oddEvenList(self, head):
    odd, even = tail = [ListNode(0), ListNode(0)]
    i = 0
    while head:
        tail[i].next = tail[i] = head
        head = head.next
        i ^= 1
    tail[0].next = even.next
    tail[1].next = None
    return odd.next
