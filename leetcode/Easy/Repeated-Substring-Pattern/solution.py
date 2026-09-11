"""
LeetCode: Repeated Substring Pattern
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/repeated-substring-pattern/
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
