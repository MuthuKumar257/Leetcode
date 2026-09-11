/*
 * LeetCode: Search in a Binary Search Tree
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/search-in-a-binary-search-tree/
 */

class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        while(root != null){
            if(root.val == val) return root;

            if(val < root.val){
                root = root.left;
            } else {
                root = root.right;
            }
        }

        return null;
    }
}
