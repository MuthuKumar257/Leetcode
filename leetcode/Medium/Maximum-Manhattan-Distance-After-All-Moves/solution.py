"""
LeetCode: Maximum Manhattan Distance After All Moves
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/
"""

class Solution:
    def maxDistance(self, moves: str) -> int:
        r=moves.count('R')
        d=moves.count('D')
        t=moves.count('_')
        l=moves.count('L')
        u=moves.count('U')
        return abs(r-l)+abs(u-d)+t
