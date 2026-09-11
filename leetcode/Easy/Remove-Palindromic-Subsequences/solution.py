"""
LeetCode: Remove Palindromic Subsequences
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/remove-palindromic-subsequences/
"""

class Solution:
        def removePalindromeSub(self, s):
            return 2 - (s == s[::-1]) - (s == "")
