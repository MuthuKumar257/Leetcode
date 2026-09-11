"""
LeetCode: Third Maximum Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/third-maximum-number/
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) >= 3:
            return sorted(set(nums))[-3]
        else:
            return sorted(set(nums))[-1]
