"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        #reverse the first half of the linked list
        reverse, fast = None,head
        while fast and fast.next:
            fast = fast.next.next
            head.next,reverse,head = reverse,head,head.next
            
        tail = head.next if fast else head
        
        # Compare the reversed first half list with the second half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse,tail = reverse.next,tail.next
        return is_palindrome