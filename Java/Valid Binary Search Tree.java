/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
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



//O(n^2) runtime, O(n) stack space – Brute force:
public boolean isValidBST(TreeNode root) {
	if (root == null) return true;
  		return isSubtreeLessThan(root.left, root.val)
      		&& isSubtreeGreaterThan(root.right, root.val)
      		&& isValidBST(root.left) && isValidBST(root.right);
}
private boolean isSubtreeLessThan(TreeNode p, int val) {
  	if (p == null) return true;
  		return p.val < val
      		&& isSubtreeLessThan(p.left, val)
      		&& isSubtreeLessThan(p.right, val);
}

private boolean isSubtreeGreaterThan(TreeNode p, int val) {
  	if (p == null) return true;
  		return p.val > val
		&& isSubtreeGreaterThan(p.left, val)
		&& isSubtreeGreaterThan(p.right, val);
}

//O(n) runtime, O(n) stack space – Top-down recursion:
public class Solution {
    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        return isValidBSTRecu(root,null,null);
    }
    
    private boolean isValidBSTRecu(TreeNode root,Integer low,Integer high)
    {
        if(root == null) return true;
        if((low != null && root.val <= low)  || (high != null && root.val >= high)) return false;
        return isValidBSTResu(root.left,low,root.val) && isValidBSTResu(root.right,root.val,high);
    }
}

//O(n) runtime, O(n) stack space – In-order traversal:
public class Solution {
    private TreeNode prev;
    public boolean isValidBST(TreeNode root) {
        prev = null;
        return isMonotonicIncreasing(root);
    }
    
    private boolean isMonotonicIncreasing(TreeNode p)
    {
        if(p == null) return true;
        if(isMonotonicIncreasing(p.left))
        {
            if(prev != null && prev.val >= p.val) return false;
            prev = p;
            return isMonotonicIncreasing(p.right);
        }
        else
            return false;
    }
}