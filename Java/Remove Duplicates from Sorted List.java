/*
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        if(head == null) return head;
        ListNode dummy = new ListNode(head.val+1);
        dummy.next = head;
        
        ListNode prev = dummy;
        ListNode cur = dummy.next;
        while(cur != null){
            if(prev.val == cur.val){
                prev.next = cur.next;
                cur = cur.next;
            }
            else{
                cur = cur.next;
                prev = prev.next;
            }
        }
        
        return dummy.next;
    }
}