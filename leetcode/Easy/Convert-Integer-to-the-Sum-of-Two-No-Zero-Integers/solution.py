"""
LeetCode: Convert Integer to the Sum of Two No-Zero Integers
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next((k,n-k) for k in range(n) if '0' not in f'{k}{n-k}')
