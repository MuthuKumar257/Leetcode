"""
LeetCode: Find the Difference
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-the-difference/
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(x) for x in s)
        t_sum = sum(ord(y) for y in t)
    
        return chr(t_sum - s_sum)
