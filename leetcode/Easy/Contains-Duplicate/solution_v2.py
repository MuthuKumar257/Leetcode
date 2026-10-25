"""
LeetCode: Contains Duplicate
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
