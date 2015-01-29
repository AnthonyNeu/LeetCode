"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = ListNode(0)
        pre = None
        carry = 0
        while l1 and l2:
            carry = l1.val + l2.val + carry
            r = ListNode(carry % 10)
            if pre:
                pre.next = r
                pre = pre.next
            else:
                pre,result = r,r
            carry = carry/10
            l1 = l1.next
            l2 = l2.next
        while l1:
            carry = l1.val + carry
            r = ListNode(carry % 10)
            pre.next = r
            pre = pre.next
            carry = carry/10
            l1 = l1.next
        while l2:
            carry = l2.val + carry
            r = ListNode(carry % 10)
            pre.next = r
            pre = pre.next
            carry = carry/10
            l2 = l2.next
        if carry>0:
            r = ListNode(carry)
            pre.next = r
        return result