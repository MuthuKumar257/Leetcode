// Last updated: 9/11/2026, 9:41:42 AM
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