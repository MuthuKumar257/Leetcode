"""
LeetCode: Maximum Nesting Depth of Two Valid Parentheses Strings
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
"""

class Solution:
    def maxDepthAfterSplit(self, seq: str):
        return [(i + (c == '(')) % 2 for i, c in enumerate(seq)]
