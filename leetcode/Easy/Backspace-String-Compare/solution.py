"""
LeetCode: Backspace String Compare
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)
