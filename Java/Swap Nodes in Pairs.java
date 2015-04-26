/*
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while(head != null && head.next != null)
        {
            ListNode p1 = head.next;
            ListNode p2 = head.next.next;
            //link the pair node to the previous head
            prev.next = p1;
            p1.next = head;
            head.next = p2;
            //set the prev and head
            prev = head;
            head = p2;
        }
        return dummy.next;
    }
}
