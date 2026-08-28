// Last updated: 8/28/2026, 9:34:14 AM
1class Solution {
2    private int maxSum = Integer.MIN_VALUE;
3
4    public int maxPathSum(TreeNode root) {
5        helper(root);
6        return maxSum;
7    }
8
9    private int helper(TreeNode node) {
10        if (node == null) {
11            return 0;
12        }
13
14        int leftMaxPath = Math.max(helper(node.left), 0);
15        int rightMaxPath = Math.max(helper(node.right), 0);
16
17        int maxIfNodeIsRoot = node.val + leftMaxPath + rightMaxPath;
18        maxSum = Math.max(maxSum, maxIfNodeIsRoot);
19
20        return node.val + Math.max(leftMaxPath, rightMaxPath);
21    }
22}