"""
LeetCode: Number of 1 Bits
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        a=str(bin(n))[2:]
        return a.count('1')
