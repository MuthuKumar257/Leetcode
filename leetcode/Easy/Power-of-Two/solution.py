"""
LeetCode: Power of Two
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/power-of-two/
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        for i in range(31):
            if n==2**i:
                return True
        return False
