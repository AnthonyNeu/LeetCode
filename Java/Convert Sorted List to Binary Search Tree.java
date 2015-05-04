/*
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//O(n) runtime, O(log n) stack space – Bottom-up recursion:
public class Solution {
    private ListNode list;
    
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) return null;
        int number = 0;
        ListNode p = head;
        while(p!=null){
            p = p.next;
            number ++;
        }
        list = head;
        return sortedListToBST(0,number-1);
    }
    
    private TreeNode sortedListToBST(int start,int end){
        if(start > end) return null;
        int mid = start + (end - start)/2;
        TreeNode leftchild = sortedListToBST(start,mid-1);
        TreeNode parent = new TreeNode(list.val);
        list = list.next;
        TreeNode rightchild = sortedListToBST(mid+1,end);
        parent.left = leftchild;
        parent.right = rightchild;
        return parent;
    }
}