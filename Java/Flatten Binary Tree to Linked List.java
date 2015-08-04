/*
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
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
    public void flatten(TreeNode root) {
        if(root == null) return;
        
        flatten(root.left);
        flatten(root.right);
        
        if(root.left == null) return;
        
        TreeNode p = root.left;
        while(p.right != null) p = p.right;
        p.right = root.right;
        root.right = root.left;
        root.left = null;
    }
}

public class Solution {
    public void flatten(TreeNode root) {
        flatten(root, null);
    }
    
    private TreeNode flatten(TreeNode root, TreeNode tail){
        if(root == null) return tail;
        
        root.right = flatten(root.left, flatten(root.right, tail));
        root.left = null;
        return root;
    } 
}

public class Solution {
    public void flatten(TreeNode root) {
        if(root == null) return;
        Stack<TreeNode> stack = new Stack<>();
        
        stack.push(root);
        
        while(!stack.empty()){
            TreeNode p = stack.peek();
            stack.pop();
            
            if(p.right != null) stack.push(p.right);
            if(p.left != null) stack.push(p.left);
            
            p.left = null;
            if(!stack.empty()){
                p.right = stack.peek();
            }
        }
    }
}
