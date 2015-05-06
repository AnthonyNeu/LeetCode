/*
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left
￼node that shares the same parent node) or empty, flip it upside down and turn it into a tree
￼where the original right nodes turned into left leaf nodes. Return the new root.
*/

//Top down approach:
public TreeNode UpsideDownBinaryTree(TreeNode root) {
   	TreeNode p = root, parent = null, parentRight = null;
   	while (p != null) {
      	TreeNode left = p.left;
      	p.left = parentRight;
      	parentRight = p.right;
      	p.right = parent;
      	parent = p;
		p = left; 
	}
   	return parent;
}

//Bottom up approach:
public TreeNode UpsideDownBinaryTree(TreeNode root) {
   	return dfsBottomUp(root, null);
}

private TreeNode dfsBottomUp(TreeNode p, TreeNode parent) {
   	if (p == null) return parent;
   	TreeNode root = dfsBottomUp(p.left, p);
   	p.left = (parent == null) ? parent : parent.right;
   	p.right = parent;
   	return root;
}