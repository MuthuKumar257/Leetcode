"""
LeetCode: Spiral Matrix
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
