"""
LeetCode: Shuffle String
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/shuffle-string/
"""

class Solution:
    def restoreString(self, s: str, p: List[int]) -> str:
        return ''.join([v for (_,v) in sorted(zip(p,s))])
