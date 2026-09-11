"""
LeetCode: Water Bottles II
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/water-bottles-ii/
"""

class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        o=0
        while n>=e:
             o+=e
             n-=e-1
             e+=1
        return o+n
