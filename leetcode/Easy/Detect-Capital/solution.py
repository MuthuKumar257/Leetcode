"""
LeetCode: Detect Capital
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/detect-capital/
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())
