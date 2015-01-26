"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in range(1,n+1):
            if i < m:
                prev = prev.next
            elif i == m:
                last_swapped = prev.next
                cur = last_swapped.next
            else:
                last_swapped.next = cur.next
                cur.next = prev.next
                prev.next = cur
                cur = last_swapped.next
        return dummy.next