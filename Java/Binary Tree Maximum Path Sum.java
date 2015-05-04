/*
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
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
    private int max = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        maxPathSumRecu(root);
        return this.max;
    }
    
    private int maxPathSumRecu(TreeNode root){
        if(root == null) return 0;
        int l = Math.max(0,maxPathSumRecu(root.left));
        int r = Math.max(0,maxPathSumRecu(root.right));
        this.max = Math.max(this.max,l+r+root.val);
        return root.val + Math.max(l,r);
    }
}