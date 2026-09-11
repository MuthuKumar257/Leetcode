"""
LeetCode: Power of Four
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/power-of-four/
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            if n==4**i:
                return True
        return False
