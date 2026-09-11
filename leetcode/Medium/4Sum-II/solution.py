"""
LeetCode: 4Sum II
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/4sum-ii/
"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
