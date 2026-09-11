"""
LeetCode: Binary Tree Postorder Traversal
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
