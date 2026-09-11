"""
LeetCode: Find N Unique Integers Sum up to Zero
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))
