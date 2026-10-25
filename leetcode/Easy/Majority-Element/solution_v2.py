"""
LeetCode: Majority Element
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
