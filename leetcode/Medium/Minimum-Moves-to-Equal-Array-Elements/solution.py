"""
LeetCode: Minimum Moves to Equal Array Elements
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""

class Solution:
    def minMoves(self, nums: list[int]) -> int:
                return sum(nums) - len(nums) * min(nums)
