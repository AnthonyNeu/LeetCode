/*
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
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
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> result = new ArrayList<>();
        
        if(root != null) stack.push(root);
        
        while(!stack.empty()){
            TreeNode p = stack.peek();
            stack.pop();
            result.add(p.val);
            
            if(p.right != null) stack.push(p.right);
            if(p.left != null) stack.push(p.left);
        }
        
        return result;
        
    }
}
