"""
LeetCode: First Unique Character in a String
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        occu = {}

        for c in s:
            if c in occu:
                occu[c] += 1
            else:
                occu[c] = 1

        for i, c in enumerate(s):
            if occu[c] == 1:
                return i
        else:
            return -1
