"""
LeetCode: Maximum Depth of Binary Tree
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
