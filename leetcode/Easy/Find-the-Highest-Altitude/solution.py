"""
LeetCode: Find the Highest Altitude
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-the-highest-altitude/
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        for i in gain:
            a.append(a[len(a)-1]+i)
        return max(a)
