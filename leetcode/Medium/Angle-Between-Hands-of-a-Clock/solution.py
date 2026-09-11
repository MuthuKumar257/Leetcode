"""
LeetCode: Angle Between Hands of a Clock
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a=abs((30*hour)-(5.5*minutes))
        return min(a,360-a)
