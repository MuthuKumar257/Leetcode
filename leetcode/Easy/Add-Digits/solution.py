"""
LeetCode: Add Digits
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/add-digits/
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num == 0:
            return 0
        return 1 + (num - 1) % 9
