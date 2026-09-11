// Last updated: 9/11/2026, 9:46:30 AM
class Solution {
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        helper(root);
        return maxSum;
    }

    private int helper(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftMaxPath = Math.max(helper(node.left), 0);
        int rightMaxPath = Math.max(helper(node.right), 0);

        int maxIfNodeIsRoot = node.val + leftMaxPath + rightMaxPath;
        maxSum = Math.max(maxSum, maxIfNodeIsRoot);

        return node.val + Math.max(leftMaxPath, rightMaxPath);
    }
}