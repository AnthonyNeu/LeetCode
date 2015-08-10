/*
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        
        pathSum(result, cur, root, sum);
        return result;
    }
    
    private void pathSum(List<List<Integer>> result, List<Integer> cur, TreeNode root, int sum){
        if(root == null) return;
        
        if(root.right == null && root.left == null && root.val == sum){
            cur.add(root.val);
            result.add(new ArrayList<Integer>(cur));
            cur.remove(cur.size() - 1);
            return;
        }
        
        cur.add(root.val);
        pathSum(result, cur, root.left, sum - root.val);
        pathSum(result, cur, root.right, sum - root.val);
        cur.remove(cur.size() - 1);
    }
}