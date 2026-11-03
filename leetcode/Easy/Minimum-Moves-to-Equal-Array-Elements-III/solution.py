"""
LeetCode: Minimum Moves to Equal Array Elements III
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        res = 0
        for x in nums:
            res += mx - x
        return res
