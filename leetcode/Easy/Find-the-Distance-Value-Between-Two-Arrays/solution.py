"""
LeetCode: Find the Distance Value Between Two Arrays
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
"""

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(d<min(abs(v-u) for u in b) for v in a)
