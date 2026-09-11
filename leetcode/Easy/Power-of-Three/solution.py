"""
LeetCode: Power of Three
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/power-of-three/
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if n==3**i:
                return True
        return False
