// Last updated: 8/11/2026, 6:41:42 PM
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