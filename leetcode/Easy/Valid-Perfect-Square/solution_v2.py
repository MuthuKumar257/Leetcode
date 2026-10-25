"""
LeetCode: Valid Perfect Square
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/valid-perfect-square/
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num))**2==num
