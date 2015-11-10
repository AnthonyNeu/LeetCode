/*
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
*/


/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */

// use recursion
class Solution1 {
public:
    void connect(TreeLinkNode *root) {
        if (root == nullptr) {
            return;
        }
        TreeLinkNode dummy = TreeLinkNode(-1);
        for (TreeLinkNode *prev = &dummy, *cur = root ; cur != nullptr ; cur = cur -> next) {
            if (cur -> left) {
                prev -> next = cur -> left;
                prev = prev -> next;
            }
            if (cur -> right) {
                prev -> next = cur -> right;
                prev = prev -> next;
            }
        }
        connect(dummy.next);
    }
};

// use level order traversal
class Solution2 {
public:
    void connect(TreeLinkNode *root) {
        while (root != nullptr) {
            /**
             * prev for previous node in this level, first for the first node in next level
             **/
            TreeLinkNode *prev = nullptr;
            TreeLinkNode *first = nullptr;
            
            for(; root != nullptr ; root = root -> next){
                if (first == nullptr) first = root -> left != nullptr ? root -> left : root -> right;
                
                if(root -> left != nullptr){
                    if (prev != nullptr) prev -> next = root -> left;
                    prev = root -> left;
                }
                
                if(root -> right != nullptr){
                    if(prev != nullptr) prev -> next = root -> right;
                    prev = root -> right;
                }
            }
            
            root = first;
        }
    }
};
