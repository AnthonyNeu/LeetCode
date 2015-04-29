/*


*/

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */

//O(n) time, O(n) space: Hash table
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        HashMap<RandomListNode,RandomListNode> map = new HashMap<>();
        RandomListNode dummy = new RandomListNode(0);
        dummy.next = head;
        RandomListNode current = head;
        RandomListNode newList = dummy;
        while(current != null)
        {
            newList.next = new RandomListNode(current.label);
            map.put(current,newList.next);
            newList = newList.next;
            current = current.next;
        }
        newList = dummy;
        current = head;
        while(current != null)
        {
            newList.next.random = map.get(current.random);
            newList = newList.next;
            current = current.next;
        }
        return dummy.next;
    }
}

//O(n) time, O(1) space:
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode p = head;
        while(p != null)
        {
            RandomListNode next = p.next;
            RandomListNode copy = new RandomListNode(p.label);
            p.next = copy;
            copy.next= next;
            p = next;
        }
        p = head;
        while(p != null)
        {
            p.next.random = (p.random != null) ? p.random.next : null;
            p = p.next.next;
        }
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode prev = dummy;
        p = head;
        while(p != null)
        {
            RandomListNode copy = p.next;
            p.next = copy.next;
            prev.next = copy;
            p = p.next;
            prev = prev.next;
        }
        return dummy.next;
    }
}