/*
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
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
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        if(p != null && q == null) return false;
        if(p == null && q != null) return false;
        
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}


public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<>();
        stack.push(p);
        stack.push(q);
        
        while(!stack.empty()){
            p = stack.peek();
            stack.pop();
            q = stack.peek();
            stack.pop();
            
            if(p == null && q == null) continue;
            if(p == null || q == null) return false;
            if(p.val != q.val) return false;
            
            stack.push(p.left);
            stack.push(q.left);
            
            stack.push(p.right);
            stack.push(q.right);
        }
        
        return true;
    }
}