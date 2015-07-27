/*
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) return head;
        int length = 1;
        ListNode cur = head;
        while(cur.next != null){
            length ++;
            cur = cur.next;
        }
        
        k %= length;
        cur.next = head;
        for(int i = 0 ; i < length - k ; i ++){
            cur = cur.next;
        }
        head = cur.next;
        cur.next = null;
        return head;
    }
}
