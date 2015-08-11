/*
Sort a linked list in O(n log n) time using constant space complexity.
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
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null) return head;
        
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        
        fast = slow;
        slow = slow.next;
        fast.next = null;
        
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        
        return mergeTwoLists(l1, l2);
    }
    
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode prev = dummy;
        while(l1 != null && l2 != null)
        {
            if(l1.val <= l2.val)
            {
                prev.next = l1;
                l1 = l1.next;
            }
            else
            {
                prev.next = l2;
                l2 = l2.next;
            }
            prev = prev.next;
        }
        if(l1 != null) prev.next = l1;
        if(l2 != null) prev.next = l2;
        return dummy.next;
    }
}