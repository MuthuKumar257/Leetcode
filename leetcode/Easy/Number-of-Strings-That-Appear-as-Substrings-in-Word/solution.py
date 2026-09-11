"""
LeetCode: Number of Strings That Appear as Substrings in Word
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for i in patterns:
            if i in word:
                c+=1
        return c
