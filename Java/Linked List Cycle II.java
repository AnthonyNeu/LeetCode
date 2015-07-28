/*
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?

When fast is met with slow, assume fast has traveled the the cycle for n times. Suppose the cycle has length r and slow has traveled length s:
2 * s = n * r + s;

Suppose the length of list of L and the length from head to the head of cycle is a and the meeting point is x away from the head of cycle:

a + x = s = n * r = (n - 1) * r + r = (n - 1) * r + L - a

a = (n - 1) * r + (L - a - x)

L - a - x is the distance from the meeting point to the head of cycle. So the head of list is equal to the n-1 times of length of cycle and 
the length from the meeting point to the head of cycle. So we set another slow ListNode from the head of list and move the two slow ListNode 
together, they will meet at the head of the cycle.

*/


/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            
            if(fast == slow){
                ListNode slow2 = head;
                while(slow2 != slow){
                    slow2 = slow2.next;
                    slow = slow.next;
                }
                return slow2;
            }
        }
        return null;
    }
}