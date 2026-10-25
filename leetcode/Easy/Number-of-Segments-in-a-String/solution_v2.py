"""
LeetCode: Number of Segments in a String
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/number-of-segments-in-a-string/
"""

class Solution:
    def countSegments(self, s: str) -> int:
        arr=s.split()
        return len(arr)
