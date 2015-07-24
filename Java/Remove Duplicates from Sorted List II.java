/*
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null) return head;
        
        ListNode p = head.next;
        if(head.val == p.val){
            while(p != null && head.val == p.val){
                head.next = p.next;
                p = p.next;
            }
            return deleteDuplicates(p);
        }
        else{
            head.next = deleteDuplicates(head.next);
            return head;
        }
    }
}


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        
        ListNode dummy = new ListNode(head.val);
        dummy.next = head;
        
        ListNode prev = dummy;
        ListNode cur = dummy.next;
        while(cur != null){
            boolean isDuplicate = false;
            while(cur.next != null && cur.val == cur.next.val){
                isDuplicate = true;
                prev.next = cur.next;
                cur = cur.next;
            }
            //if duplicated, delete the cur
            if(isDuplicate){
                prev.next = cur.next;
                cur = cur.next;
            }
            //if not, move prev and cur
            else{
                prev = prev.next;
                cur = cur.next;
            }
        }
        
        return dummy.next;
    }
}