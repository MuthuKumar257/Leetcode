"""
LeetCode: Smallest Missing Multiple of K
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/smallest-missing-multiple-of-k/
"""

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        cur = k
        while cur in seen:
            cur += k

        return cur
