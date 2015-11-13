/*
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        if(!root) return result;
    
        binaryTreePaths(result, root, to_string(root->val));
        return result;
    }
    
    void binaryTreePaths(vector<string>& result, TreeNode* root, string t) {
        if (!root -> left && !root -> right) {
            result.push_back(t);
            return;
        }
        
        if (root -> left) binaryTreePaths(result, root -> left, t + "->" + to_string(root -> left -> val));
        if (root -> right) binaryTreePaths(result, root -> right, t + "->" + to_string(root -> right -> val));
    }
};