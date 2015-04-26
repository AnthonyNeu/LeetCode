/*
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

//O(nk log k) runtime, O(1) space – Divide and conquer using two way merge:
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;
        int end = lists.length -1;
        while(end > 0)
        {
            int begin = 0;
            while(begin < end)
            {
                lists[begin] = mergeTwoLists(lists[begin],lists[end]);
                begin++;
                end--;
            }
        }
        return lists[0];
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


//O(nk log k) runtime, O(k) space – Heap:
public class Solution {
    private static final Comparator<ListNode> listComparator =
      new Comparator<ListNode>() {
        @Override
        public int compare(ListNode x, ListNode y) {
            return x.val - y.val;
        }
    };
    
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        Queue<ListNode> queue = new PriorityQueue<>(lists.length, listComparator); 
        for (ListNode node : lists) {
            if (node != null) {
                queue.add(node);
            } 
        }
        ListNode dummyHead = new ListNode(0);
        ListNode p = dummyHead;
        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            p.next = node;
            p = p.next;
            if (node.next != null) {
                queue.add(node.next);
            }
        }
        return dummyHead.next;
    }
}