/*
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder.length == 0) return null;
        
        TreeNode root = new TreeNode(postorder[postorder.length - 1]);
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        int idx1 = postorder.length - 2;
        int idx2 = inorder.length - 1;
        while(true){
            if(inorder[idx2] == stack.peek().val){
                TreeNode p = stack.pop();
                if(--idx2 < 0) break;
                if(!stack.isEmpty() && inorder[idx2] == stack.peek().val) continue;
                p.left = new TreeNode(postorder[idx1--]);
                stack.push(p.left);
            }
            else{
                TreeNode p = new TreeNode(postorder[idx1--]);
                stack.peek().right = p;
                stack.push(p);
            }
        }
        
        return root;
    }
}