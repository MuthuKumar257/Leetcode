"""
LeetCode: Binary Prefix Divisible By 5
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/binary-prefix-divisible-by-5/
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for bit in nums:
            cur = ((cur << 1) + bit) % 5
            res.append(cur == 0)
        return res
