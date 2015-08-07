/*
Given preorder and inorder traversal of a tree, construct the binary tree.

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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(inorder.length == 0) return null;
        
        TreeNode root = new TreeNode(preorder[0]);
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        int idx1 = 0;
        int idx2 = 1;
        while(true){
            if(inorder[idx1] == stack.peek().val){
                TreeNode p = stack.pop();
                idx1++;
                if(idx1 == inorder.length) break;
                if(!stack.isEmpty() && stack.peek().val == inorder[idx1]) continue;
                p.right = new TreeNode(preorder[idx2]);
                idx2++;
                stack.push(p.right);
            }
            else{
                TreeNode p = new TreeNode(preorder[idx2]);
                idx2++;
                stack.peek().left = p;
                stack.push(p);
            }
        }
        
        return root;
    }
}
