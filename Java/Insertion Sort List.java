/*
Sort a linked list using insertion sort.
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
    public ListNode insertionSortList(ListNode head) {
        if(head == null) return head;
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        //notice that we cannot connect head to dummy.next, as this will cause the first for loop to produce cur -> cur then time limit exceed
        //dummy.next = head;

        for(ListNode cur = head ; cur != null ;){
            ListNode pos = findInsertPosition(dummy, cur.val);
            ListNode next = cur.next;
            cur.next = pos.next;
            pos.next = cur;
            cur = next;
        }
        
        return dummy.next;
    }
    
    private ListNode findInsertPosition(ListNode head, int val){
        ListNode prev = null;
        for(ListNode cur = head ; cur != null && cur.val <= val ;){
            prev = cur;
            cur = cur.next;
        }
        return prev;
    }
}