"""
LeetCode: Check ASCII Palindromic
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/check-ascii-palindromic/
"""

class Solution:
    def isPalindromic(self, s: str) -> bool:
        b="".join(format(ord(c),'08b') for c in s)
        return b==b[::-1]
