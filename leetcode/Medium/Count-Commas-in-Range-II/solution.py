"""
LeetCode: Count Commas in Range II
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/count-commas-in-range-ii/
"""

class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n+1-1000)+max(0, n+1-int(1e6))+max(0, n+1-int(1e9))+max(0, n+1-int(1e12))+max(0, n+1-int(1e15))
