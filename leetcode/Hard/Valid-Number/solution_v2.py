"""
LeetCode: Valid Number
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/valid-number/
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$',s))
