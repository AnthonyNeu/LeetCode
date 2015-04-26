/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        int carry = 0;
        while(l1 != null || l2 != null)
        {
            int x = (l1 != null) ? l1.val:0;
            int y = (l2 != null) ? l2.val:0;
            prev.next = new ListNode((carry+x+y)%10);
            carry = (carry + x + y)/10;
            prev = prev.next;
            l1 = (l1 != null)? l1.next:null;
            l2 = (l2 != null)? l2.next:null;
        }
        if(carry>0)
        {
            prev.next = new ListNode(carry);
        }
        return dummy.next;
    }
}