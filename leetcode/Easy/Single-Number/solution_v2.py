"""
LeetCode: Single Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            s=s^nums[i]
        return s
