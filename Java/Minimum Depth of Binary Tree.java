/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
*/

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//O(n) runtime, O(log n) space – Depth-first traversal:
public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        if(root.left == null) return 1 + minDepth(root.right);
        if(root.right == null) return 1 + minDepth(root.left);
        return 1 + Math.min(minDepth(root.left),minDepth(root.right));
    }
}

//O(n) runtime, O(n) space – Breath-first traversal:
public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q= new LinkedList<>();
        q.add(root);
        int depth = 1;
        TreeNode rightmost = root;
        while(!q.isEmpty())
        {
            TreeNode p = q.poll();
            if(p.left == null && p.right == null) break;
            if(p.left != null) q.add(p.left);
            if(p.right != null) q.add(p.right);
            if(p == rightmost)
            {
                depth++;
                rightmost = (p.right != null) ? p.right:p.left;
            }
        }
        return depth;
    }
}