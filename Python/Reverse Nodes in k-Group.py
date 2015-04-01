"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        reverseTimes = self.length(head)/k
        
        dummy = ListNode(0)
        dummy.next,prev,cur = head,dummy,head
        while reverseTimes > 0:
            for i in xrange(k-1):
                move = cur.next
                cur.next = move.next
                move.next = prev.next
                prev.next = move
            prev = cur
            cur = cur.next
            reverseTimes -=1
        return dummy.next
        
    def length(self,head):
        count = 0
        while head:
            head = head.next
            count +=1
        return count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        
        cur, cur_dummy = head, dummy
        length = 0
        
        while cur:
            next_cur = cur.next
            length = (length + 1) % k
            
            if length == 0:
                next_dummy = cur_dummy.next
                self.reverse(cur_dummy, cur.next)
                cur_dummy = next_dummy
                
            cur = next_cur
            
        return dummy.next
    
    def reverse(self, begin, end):
            first = begin.next
            cur = first.next
            
            while cur != end:
                first.next = cur.next
                cur.next = begin.next
                begin.next = cur
                cur = first.next