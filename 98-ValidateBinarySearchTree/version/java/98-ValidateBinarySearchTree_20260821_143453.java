// Last updated: 8/21/2026, 2:34:53 PM
1class Solution {
2    TreeNode prev;
3        
4    public boolean isValidBST(TreeNode root) {
5        if (root == null)
6            return true;
7        
8        if(!isValidBST(root.left))
9            return false;
10        
11        if (prev != null && prev.val >= root.val)
12            return false;
13        
14        prev = root;
15        
16        if (!isValidBST(root.right))
17            return false;
18        
19        return true;
20        
21        
22    }
23}