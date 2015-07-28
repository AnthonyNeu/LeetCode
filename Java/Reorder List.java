/*
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        
        //get the length
        int length = 0;
        ListNode p = head;
        while(p != null){
            p = p.next;
            length ++;
        }
        
        //find the middle node
        p = head;
        for(int i = 0 ; i < length/2 ; i++){
             p = p.next;
        }
        
        //break into two lists
        ListNode halfHead = p.next;
        p.next = null;
        ListNode newHalfHead = reverse(halfHead);

        //combine two lists
        p = head;
        while(newHalfHead != null){
            ListNode next1 = p.next;
            ListNode next2 = newHalfHead.next;
            p.next = newHalfHead;
            newHalfHead.next = next1;
            p = next1;
            newHalfHead = next2;
        }
    }
    
    private ListNode reverse(ListNode head){
        if(head == null) return head;
        ListNode prev = null;
        ListNode cur = head;
        while(cur != null){
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}



public class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        slow = reverse(slow);
        
        //combine two lists
        ListNode cur = head;
        while(cur.next != null){
            ListNode next = cur.next;
            cur.next = slow;
            slow = slow.next;
            cur.next.next = next;
            cur = next;
        }
        cur.next = slow;
    }
    
    private ListNode reverse(ListNode head){
        if(head == null) return head;
        ListNode prev = null;
        ListNode cur = head;
        while(cur != null){
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
}