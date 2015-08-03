/*
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
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
    public void recoverTree(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<TreeNode> result = new ArrayList<>();
        
        while(!stack.empty() || root != null){
            if(root != null){
                stack.push(root);
                root = root.left;
            }
            else{
                root = stack.peek();
                stack.pop();
                result.add(root);
                root = root.right;
            }
        }
        
        TreeNode prev = null, first = null, second = null;
        for(TreeNode node : result){
            if(prev == null){
                prev = node;
            }
            else if(first == null && prev.val >= node.val){
                first = prev;
                second = node;
            }
            else if(first != null && prev.val >= node.val){
                second = node;
                break;
            }
            prev = node;
        }
        
        int val = first.val;
        first.val = second.val;
        second.val = val;
    }
}